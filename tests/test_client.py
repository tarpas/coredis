from __future__ import annotations

from ssl import SSLContext

import pytest
from packaging.version import Version

import coredis
from coredis.exceptions import CommandNotSupportedError
from tests.conftest import targets


@targets(
    "redis_basic",
    "redis_basic_resp3",
    "redis_basic_raw",
    "redis_basic_raw_resp3",
    "redis_ssl",
    "redis_ssl_resp3",
)
@pytest.mark.asyncio
class TestClient:
    @pytest.fixture(autouse=True)
    async def configure_client(self, client):
        client.verify_version = True
        await client.ping()

    async def test_custom_response_callback(self, client, _s):
        client.set_response_callback(_s("PING"), lambda r, **_: _s("BING"))
        assert await client.ping() == _s("BING")

    @pytest.mark.min_server_version("6.0.0")
    async def test_server_version(self, client):
        assert isinstance(client.server_version, Version)
        await client.ping()
        assert isinstance(client.server_version, Version)

    @pytest.mark.max_server_version("6.0.0")
    async def test_server_version_not_found(self, client):
        assert client.server_version is None
        await client.ping()
        assert client.server_version is None

    @pytest.mark.min_server_version("6.0.0")
    @pytest.mark.max_server_version("6.2.0")
    async def test_unsupported_command_6_0_x(self, client):
        await client.ping()
        with pytest.raises(CommandNotSupportedError):
            await client.getex("test")

    @pytest.mark.min_server_version("6.2.0")
    @pytest.mark.max_server_version("6.2.9")
    async def test_unsupported_command_6_2_x(self, client):
        await client.ping()
        with pytest.raises(CommandNotSupportedError):
            await client.function_list()

    @pytest.mark.min_server_version("6.2.0")
    @pytest.mark.parametrize("client_arguments", [({"db": 1})])
    async def test_select_database(self, client, client_arguments):
        assert (await client.client_info())["db"] == 1

    @pytest.mark.min_server_version("6.2.0")
    @pytest.mark.parametrize("client_arguments", [({"client_name": "coredis"})])
    async def test_set_client_name(self, client, client_arguments):
        assert (await client.client_info())["name"] == "coredis"


class TestSSL:
    async def test_explicit_ssl_parameters(self, redis_ssl_server):
        client = coredis.Redis(
            port=8379,
            ssl=True,
            ssl_keyfile="./tests/tls/client.key",
            ssl_certfile="./tests/tls/client.crt",
            ssl_ca_certs="./tests/tls/ca.crt",
        )
        assert await client.ping() == b"PONG"

    async def test_explicit_ssl_context(self, redis_ssl_server):
        context = SSLContext()
        context.load_cert_chain(
            certfile="./tests/tls/client.crt", keyfile="./tests/tls/client.key"
        )
        client = coredis.Redis(
            port=8379,
            ssl_context=context,
        )
        assert await client.ping() == b"PONG"
