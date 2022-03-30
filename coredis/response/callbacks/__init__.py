"""
coredis.response.callbacks
--------------------------
"""
from __future__ import annotations

import datetime
from abc import ABC, abstractmethod

from coredis.typing import (
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    ParamSpec,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)
from coredis.utils import nativestr

R = TypeVar("R")
P = ParamSpec("P")


class SimpleCallback(ABC):
    def __call__(self, response: Any, version: int = 2) -> Any:
        if version == 3:
            return self.transform_3(response)
        return self.transform(response)

    @abstractmethod
    def transform(self, response: Any) -> Any:
        pass

    def transform_3(self, response: Any) -> Any:
        return self.transform(response)


class ParametrizedCallback(ABC):
    def __call__(self, response: Any, version: int = 2, **kwargs: Any) -> Any:
        if version == 3:
            return self.transform_3(response, **kwargs)
        return self.transform(response, **kwargs)

    @abstractmethod
    def transform(self, response: Any, **kwargs: Any) -> Any:
        pass

    def transform_3(self, response: Any, **kwargs: Any) -> Any:
        return self.transform(response, **kwargs)


class SimpleStringCallback(SimpleCallback):
    def __init__(self, raise_on_error: Optional[Type[Exception]] = None):
        self.raise_on_error = raise_on_error

    def transform(self, response: Any) -> Any:
        success = response and nativestr(response) == "OK"
        if not success and self.raise_on_error:
            raise self.raise_on_error(response)
        return success


class PrimitiveCallback(SimpleCallback, Generic[R]):
    @abstractmethod
    def transform(self, response: Any) -> Any:
        pass


class FloatCallback(PrimitiveCallback[float]):
    def transform(self, response: Any) -> float:
        return response if isinstance(response, float) else float(response)


class BoolCallback(PrimitiveCallback[bool]):
    def transform(self, response: Any) -> bool:
        if isinstance(response, bool):
            return response
        return bool(response)


class SimpleStringOrIntCallback(SimpleCallback):
    def transform(self, response: Any) -> Union[bool, int]:
        if isinstance(response, (int, bool)):
            return response
        else:
            return SimpleStringCallback()(response)


class TupleCallback(PrimitiveCallback[Tuple]):
    def transform(self, response: Any) -> Tuple:
        return tuple(response)


class ListCallback(PrimitiveCallback[List]):
    def transform(self, response: Any) -> List:
        if isinstance(response, list):
            return response
        return list(response)


class DateTimeCallback(ParametrizedCallback):
    def transform(self, response: Any, **kwargs: Any) -> datetime.datetime:
        ts = response
        if kwargs.get("unit") == "milliseconds":
            ts = ts / 1000.0
        return datetime.datetime.fromtimestamp(ts)


class DictCallback(PrimitiveCallback[Dict]):
    def __init__(
        self,
        transform_function: Optional[Callable[[Any], Dict]] = None,
    ):
        self.transform_function = transform_function

    def transform(self, response: Any) -> Dict:
        return (
            (response if isinstance(response, dict) else dict(response))
            if not self.transform_function
            else self.transform_function(response)
        )


class SetCallback(PrimitiveCallback[Set]):
    def transform(self, response: Any) -> Set:
        if isinstance(response, set):
            return response
        return set(response) if response else set()


class BoolsCallback(SimpleCallback):
    def transform(self, response: Any) -> Tuple[bool, ...]:
        return tuple(BoolCallback()(r) for r in response)


class OptionalPrimitiveCallback(SimpleCallback, Generic[R]):
    def transform(self, response: Any) -> Optional[R]:
        return response


class OptionalFloatCallback(OptionalPrimitiveCallback[float]):
    def transform(self, response: Any) -> Optional[float]:
        if isinstance(response, float):
            return response
        return response and float(response)


class OptionalIntCallback(OptionalPrimitiveCallback[int]):
    def transform(self, response: Any) -> Optional[int]:
        if isinstance(response, int):
            return response
        return response and int(response)


class OptionalSetCallback(OptionalPrimitiveCallback[Set]):
    def transform(self, response: Any) -> Optional[Set]:
        if isinstance(response, set):
            return response
        return response and set(response)


class OptionalTupleCallback(OptionalPrimitiveCallback[Tuple]):
    def transform(self, response: Any) -> Optional[Tuple]:
        return response and tuple(response)
