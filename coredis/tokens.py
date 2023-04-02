from __future__ import annotations

from coredis._utils import CaseAndEncodingInsensitiveEnum


class PureToken(CaseAndEncodingInsensitiveEnum):
    """
    Enum for using pure-tokens with the redis api.
    """

    #: Used by:
    #:
    #:  - ``ACL LOG``
    RESET = b"RESET"

    #: Used by:
    #:
    #:  - ``BGSAVE``
    SCHEDULE = b"SCHEDULE"

    #: Used by:
    #:
    #:  - ``BITCOUNT``
    #:  - ``BITPOS``
    BIT = b"BIT"

    #: Used by:
    #:
    #:  - ``BITCOUNT``
    #:  - ``BITPOS``
    BYTE = b"BYTE"

    #: Used by:
    #:
    #:  - ``BITFIELD``
    FAIL = b"FAIL"

    #: Used by:
    #:
    #:  - ``BITFIELD``
    SAT = b"SAT"

    #: Used by:
    #:
    #:  - ``BITFIELD``
    WRAP = b"WRAP"

    #: Used by:
    #:
    #:  - ``BITOP``
    AND = b"AND"

    #: Used by:
    #:
    #:  - ``BITOP``
    NOT = b"NOT"

    #: Used by:
    #:
    #:  - ``BITOP``
    OR = b"OR"

    #: Used by:
    #:
    #:  - ``BITOP``
    XOR = b"XOR"

    #: Used by:
    #:
    #:  - ``BLMOVE``
    #:  - ``BLMPOP``
    #:  - ``LMOVE``
    #:  - ``LMPOP``
    LEFT = b"LEFT"

    #: Used by:
    #:
    #:  - ``BLMOVE``
    #:  - ``BLMPOP``
    #:  - ``LMOVE``
    #:  - ``LMPOP``
    RIGHT = b"RIGHT"

    #: Used by:
    #:
    #:  - ``BZMPOP``
    #:  - ``TS.ADD``
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    #:  - ``ZINTER``
    #:  - ``ZINTERSTORE``
    #:  - ``ZMPOP``
    #:  - ``ZUNION``
    #:  - ``ZUNIONSTORE``
    MAX = b"MAX"

    #: Used by:
    #:
    #:  - ``BZMPOP``
    #:  - ``TS.ADD``
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    #:  - ``ZINTER``
    #:  - ``ZINTERSTORE``
    #:  - ``ZMPOP``
    #:  - ``ZUNION``
    #:  - ``ZUNIONSTORE``
    MIN = b"MIN"

    #: Used by:
    #:
    #:  - ``CLIENT CACHING``
    #:  - ``CLIENT KILL``
    #:  - ``SCRIPT DEBUG``
    NO = b"NO"

    #: Used by:
    #:
    #:  - ``CLIENT CACHING``
    #:  - ``CLIENT KILL``
    #:  - ``SCRIPT DEBUG``
    YES = b"YES"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    #:  - ``CLIENT LIST``
    MASTER = b"MASTER"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    #:  - ``CLIENT LIST``
    NORMAL = b"NORMAL"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    #:  - ``CLIENT LIST``
    PUBSUB = b"PUBSUB"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    #:  - ``CLIENT LIST``
    REPLICA = b"REPLICA"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    SLAVE = b"SLAVE"

    #: Used by:
    #:
    #:  - ``CLIENT NO-EVICT``
    #:  - ``CLIENT NO-TOUCH``
    #:  - ``CLIENT REPLY``
    #:  - ``CLIENT TRACKING``
    OFF = b"OFF"

    #: Used by:
    #:
    #:  - ``CLIENT NO-EVICT``
    #:  - ``CLIENT NO-TOUCH``
    #:  - ``CLIENT REPLY``
    #:  - ``CLIENT TRACKING``
    ON = b"ON"

    #: Used by:
    #:
    #:  - ``CLIENT PAUSE``
    ALL = b"ALL"

    #: Used by:
    #:
    #:  - ``CLIENT PAUSE``
    WRITE = b"WRITE"

    #: Used by:
    #:
    #:  - ``CLIENT REPLY``
    SKIP = b"SKIP"

    #: Used by:
    #:
    #:  - ``CLIENT TRACKING``
    BCAST = b"BCAST"

    #: Used by:
    #:
    #:  - ``CLIENT TRACKING``
    NOLOOP = b"NOLOOP"

    #: Used by:
    #:
    #:  - ``CLIENT TRACKING``
    OPTIN = b"OPTIN"

    #: Used by:
    #:
    #:  - ``CLIENT TRACKING``
    OPTOUT = b"OPTOUT"

    #: Used by:
    #:
    #:  - ``CLIENT UNBLOCK``
    ERROR = b"ERROR"

    #: Used by:
    #:
    #:  - ``CLIENT UNBLOCK``
    TIMEOUT = b"TIMEOUT"

    #: Used by:
    #:
    #:  - ``CLUSTER FAILOVER``
    #:  - ``FAILOVER``
    #:  - ``SHUTDOWN``
    #:  - ``XCLAIM``
    FORCE = b"FORCE"

    #: Used by:
    #:
    #:  - ``CLUSTER FAILOVER``
    TAKEOVER = b"TAKEOVER"

    #: Used by:
    #:
    #:  - ``CLUSTER RESET``
    HARD = b"HARD"

    #: Used by:
    #:
    #:  - ``CLUSTER RESET``
    SOFT = b"SOFT"

    #: Used by:
    #:
    #:  - ``CLUSTER SETSLOT``
    STABLE = b"STABLE"

    #: Used by:
    #:
    #:  - ``COPY``
    #:  - ``FUNCTION LOAD``
    #:  - ``FUNCTION RESTORE``
    #:  - ``MIGRATE``
    #:  - ``RESTORE``
    #:  - ``RESTORE-ASKING``
    REPLACE = b"REPLACE"

    #: Used by:
    #:
    #:  - ``EXPIRE``
    #:  - ``EXPIREAT``
    #:  - ``PEXPIRE``
    #:  - ``PEXPIREAT``
    #:  - ``ZADD``
    GT = b"GT"

    #: Used by:
    #:
    #:  - ``EXPIRE``
    #:  - ``EXPIREAT``
    #:  - ``PEXPIRE``
    #:  - ``PEXPIREAT``
    #:  - ``ZADD``
    LT = b"LT"

    #: Used by:
    #:
    #:  - ``EXPIRE``
    #:  - ``EXPIREAT``
    #:  - ``GEOADD``
    #:  - ``JSON.SET``
    #:  - ``PEXPIRE``
    #:  - ``PEXPIREAT``
    #:  - ``SET``
    #:  - ``ZADD``
    NX = b"NX"

    #: Used by:
    #:
    #:  - ``EXPIRE``
    #:  - ``EXPIREAT``
    #:  - ``GEOADD``
    #:  - ``JSON.SET``
    #:  - ``PEXPIRE``
    #:  - ``PEXPIREAT``
    #:  - ``SET``
    #:  - ``ZADD``
    XX = b"XX"

    #: Used by:
    #:
    #:  - ``FAILOVER``
    #:  - ``SHUTDOWN``
    ABORT = b"ABORT"

    #: Used by:
    #:
    #:  - ``FLUSHALL``
    #:  - ``FLUSHDB``
    #:  - ``FUNCTION FLUSH``
    #:  - ``SCRIPT FLUSH``
    ASYNC = b"ASYNC"

    #: Used by:
    #:
    #:  - ``FLUSHALL``
    #:  - ``FLUSHDB``
    #:  - ``FUNCTION FLUSH``
    #:  - ``SCRIPT DEBUG``
    #:  - ``SCRIPT FLUSH``
    SYNC = b"SYNC"

    #: Used by:
    #:
    #:  - ``FUNCTION LIST``
    WITHCODE = b"WITHCODE"

    #: Used by:
    #:
    #:  - ``FUNCTION RESTORE``
    APPEND = b"APPEND"

    #: Used by:
    #:
    #:  - ``FUNCTION RESTORE``
    FLUSH = b"FLUSH"

    #: Used by:
    #:
    #:  - ``GEOADD``
    #:  - ``ZADD``
    CHANGE = b"CH"

    #: Used by:
    #:
    #:  - ``GEODIST``
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    FT = b"FT"

    #: Used by:
    #:
    #:  - ``GEODIST``
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    KM = b"KM"

    #: Used by:
    #:
    #:  - ``GEODIST``
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    M = b"M"

    #: Used by:
    #:
    #:  - ``GEODIST``
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    MI = b"MI"

    #: Used by:
    #:
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    ANY = b"ANY"

    #: Used by:
    #:
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    #:  - ``SORT``
    #:  - ``SORT_RO``
    ASC = b"ASC"

    #: Used by:
    #:
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    #:  - ``SORT``
    #:  - ``SORT_RO``
    DESC = b"DESC"

    #: Used by:
    #:
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    WITHCOORD = b"WITHCOORD"

    #: Used by:
    #:
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    WITHDIST = b"WITHDIST"

    #: Used by:
    #:
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    WITHHASH = b"WITHHASH"

    #: Used by:
    #:
    #:  - ``GEOSEARCHSTORE``
    STOREDIST = b"STOREDIST"

    #: Used by:
    #:
    #:  - ``GETEX``
    PERSIST = b"PERSIST"

    #: Used by:
    #:
    #:  - ``HRANDFIELD``
    WITHVALUES = b"WITHVALUES"

    #: Used by:
    #:
    #:  - ``LCS``
    IDX = b"IDX"

    #: Used by:
    #:
    #:  - ``LCS``
    LEN = b"LEN"

    #: Used by:
    #:
    #:  - ``LCS``
    WITHMATCHLEN = b"WITHMATCHLEN"

    #: Used by:
    #:
    #:  - ``LINSERT``
    AFTER = b"AFTER"

    #: Used by:
    #:
    #:  - ``LINSERT``
    BEFORE = b"BEFORE"

    #: Used by:
    #:
    #:  - ``MIGRATE``
    COPY = b"COPY"

    #: Used by:
    #:
    #:  - ``MIGRATE``
    EMPTY_STRING = b""

    #: Used by:
    #:
    #:  - ``RESTORE``
    #:  - ``RESTORE-ASKING``
    ABSTTL = b"ABSTTL"

    #: Used by:
    #:
    #:  - ``SET``
    GET = b"GET"

    #: Used by:
    #:
    #:  - ``SET``
    KEEPTTL = b"KEEPTTL"

    #: Used by:
    #:
    #:  - ``SHUTDOWN``
    NOSAVE = b"NOSAVE"

    #: Used by:
    #:
    #:  - ``SHUTDOWN``
    NOW = b"NOW"

    #: Used by:
    #:
    #:  - ``SHUTDOWN``
    SAVE = b"SAVE"

    #: Used by:
    #:
    #:  - ``SORT``
    #:  - ``SORT_RO``
    SORTING = b"ALPHA"

    #: Used by:
    #:
    #:  - ``XADD``
    #:  - ``XTRIM``
    APPROXIMATELY = b"~"

    #: Used by:
    #:
    #:  - ``XADD``
    AUTO_ID = b"*"

    #: Used by:
    #:
    #:  - ``XADD``
    #:  - ``XTRIM``
    EQUAL = b"="

    #: Used by:
    #:
    #:  - ``XADD``
    #:  - ``XTRIM``
    MAXLEN = b"MAXLEN"

    #: Used by:
    #:
    #:  - ``XADD``
    #:  - ``XTRIM``
    MINID = b"MINID"

    #: Used by:
    #:
    #:  - ``XADD``
    NOMKSTREAM = b"NOMKSTREAM"

    #: Used by:
    #:
    #:  - ``XAUTOCLAIM``
    #:  - ``XCLAIM``
    JUSTID = b"JUSTID"

    #: Used by:
    #:
    #:  - ``XGROUP CREATE``
    MKSTREAM = b"MKSTREAM"

    #: Used by:
    #:
    #:  - ``XGROUP CREATE``
    #:  - ``XGROUP SETID``
    NEW_ID = b"$"

    #: Used by:
    #:
    #:  - ``XINFO STREAM``
    FULL = b"FULL"

    #: Used by:
    #:
    #:  - ``XREADGROUP``
    NOACK = b"NOACK"

    #: Used by:
    #:
    #:  - ``ZADD``
    INCREMENT = b"INCR"

    #: Used by:
    #:
    #:  - ``ZDIFF``
    #:  - ``ZINTER``
    #:  - ``ZRANDMEMBER``
    #:  - ``ZRANGE``
    #:  - ``ZRANGEBYSCORE``
    #:  - ``ZREVRANGE``
    #:  - ``ZREVRANGEBYSCORE``
    #:  - ``ZUNION``
    WITHSCORES = b"WITHSCORES"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    #:  - ``ZINTER``
    #:  - ``ZINTERSTORE``
    #:  - ``ZUNION``
    #:  - ``ZUNIONSTORE``
    SUM = b"SUM"

    #: Used by:
    #:
    #:  - ``ZRANGE``
    #:  - ``ZRANGESTORE``
    BYLEX = b"BYLEX"

    #: Used by:
    #:
    #:  - ``ZRANGE``
    #:  - ``ZRANGESTORE``
    BYSCORE = b"BYSCORE"

    #: Used by:
    #:
    #:  - ``ZRANGE``
    #:  - ``ZRANGESTORE``
    REV = b"REV"

    #: Used by:
    #:
    #:  - ``ZRANK``
    #:  - ``ZREVRANK``
    WITHSCORE = b"WITHSCORE"

    #: Used by:
    #:
    #:  - ``BF.INSERT``
    #:  - ``BF.RESERVE``
    NONSCALING = b"NONSCALING"

    #: Used by:
    #:
    #:  - ``BF.INFO``
    #:  - ``BF.INSERT``
    #:  - ``CF.INSERT``
    #:  - ``CF.INSERTNX``
    ITEMS = b"ITEMS"

    #: Used by:
    #:
    #:  - ``BF.INSERT``
    #:  - ``CF.INSERT``
    #:  - ``CF.INSERTNX``
    NOCREATE = b"NOCREATE"

    #: Used by:
    #:
    #:  - ``BF.INFO``
    CAPACITY = b"CAPACITY"

    #: Used by:
    #:
    #:  - ``BF.INFO``
    EXPANSION = b"EXPANSION"

    #: Used by:
    #:
    #:  - ``BF.INFO``
    FILTERS = b"FILTERS"

    #: Used by:
    #:
    #:  - ``BF.INFO``
    SIZE = b"SIZE"

    #: Used by:
    #:
    #:  - ``CMS.MERGE``
    WEIGHTS = b"WEIGHTS"

    #: Used by:
    #:
    #:  - ``TOPK.LIST``
    WITHCOUNT = b"WITHCOUNT"

    #: Used by:
    #:
    #:  - ``TDIGEST.MERGE``
    COMPRESSION = b"COMPRESSION"

    #: Used by:
    #:
    #:  - ``TDIGEST.MERGE``
    OVERRIDE = b"OVERRIDE"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    BLOCK = b"BLOCK"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.CREATE``
    COMPRESSED = b"COMPRESSED"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    FIRST = b"FIRST"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    LAST = b"LAST"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.CREATE``
    #:  - ``TS.DECRBY``
    #:  - ``TS.INCRBY``
    UNCOMPRESSED = b"UNCOMPRESSED"

    #: Used by:
    #:
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    AVG = b"AVG"

    #: Used by:
    #:
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    COUNT = b"COUNT"

    #: Used by:
    #:
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    RANGE = b"RANGE"

    #: Used by:
    #:
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    STD_P = b"STD.P"

    #: Used by:
    #:
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    STD_S = b"STD.S"

    #: Used by:
    #:
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    TWA = b"TWA"

    #: Used by:
    #:
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    VAR_P = b"VAR.P"

    #: Used by:
    #:
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    VAR_S = b"VAR.S"

    #: Used by:
    #:
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    BUCKETTIMESTAMP = b"BUCKETTIMESTAMP"

    #: Used by:
    #:
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    EMPTY = b"EMPTY"

    #: Used by:
    #:
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    FILTER_BY_VALUE = b"FILTER_BY_VALUE"

    #: Used by:
    #:
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    GROUPBY = b"GROUPBY"

    #: Used by:
    #:
    #:  - ``TS.MGET``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    SELECTED_LABELS = b"SELECTED_LABELS"

    #: Used by:
    #:
    #:  - ``TS.MGET``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    WITHLABELS = b"WITHLABELS"


class PrefixToken(CaseAndEncodingInsensitiveEnum):
    """
    Enum for internal use when adding prefixes to arguments
    """

    #: Used by:
    #:
    #:  - ``BITFIELD``
    #:  - ``BITFIELD_RO``
    #:  - ``SORT``
    #:  - ``SORT_RO``
    GET = b"GET"

    #: Used by:
    #:
    #:  - ``BITFIELD``
    INCRBY = b"INCRBY"

    #: Used by:
    #:
    #:  - ``BITFIELD``
    OVERFLOW = b"OVERFLOW"

    #: Used by:
    #:
    #:  - ``BITFIELD``
    SET = b"SET"

    #: Used by:
    #:
    #:  - ``BLMPOP``
    #:  - ``BZMPOP``
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``GEORADIUSBYMEMBER_RO``
    #:  - ``GEORADIUS_RO``
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    #:  - ``HSCAN``
    #:  - ``LMPOP``
    #:  - ``LPOS``
    #:  - ``SCAN``
    #:  - ``SSCAN``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    #:  - ``XAUTOCLAIM``
    #:  - ``XINFO STREAM``
    #:  - ``XRANGE``
    #:  - ``XREAD``
    #:  - ``XREADGROUP``
    #:  - ``XREVRANGE``
    #:  - ``ZMPOP``
    #:  - ``ZSCAN``
    COUNT = b"COUNT"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    ADDR = b"ADDR"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    #:  - ``CLIENT LIST``
    IDENTIFIER = b"ID"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    LADDR = b"LADDR"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    SKIPME = b"SKIPME"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    #:  - ``CLIENT LIST``
    #:  - ``SCAN``
    TYPE = b"TYPE"

    #: Used by:
    #:
    #:  - ``CLIENT KILL``
    USER = b"USER"

    #: Used by:
    #:
    #:  - ``CLIENT SETINFO``
    LIB_NAME = b"LIB-NAME"

    #: Used by:
    #:
    #:  - ``CLIENT SETINFO``
    LIB_VER = b"LIB-VER"

    #: Used by:
    #:
    #:  - ``CLIENT TRACKING``
    PREFIX = b"PREFIX"

    #: Used by:
    #:
    #:  - ``CLIENT TRACKING``
    REDIRECT = b"REDIRECT"

    #: Used by:
    #:
    #:  - ``CLUSTER SETSLOT``
    IMPORTING = b"IMPORTING"

    #: Used by:
    #:
    #:  - ``CLUSTER SETSLOT``
    MIGRATING = b"MIGRATING"

    #: Used by:
    #:
    #:  - ``CLUSTER SETSLOT``
    NODE = b"NODE"

    #: Used by:
    #:
    #:  - ``COMMAND LIST``
    ACLCAT = b"ACLCAT"

    #: Used by:
    #:
    #:  - ``COMMAND LIST``
    FILTERBY = b"FILTERBY"

    #: Used by:
    #:
    #:  - ``COMMAND LIST``
    MODULE = b"MODULE"

    #: Used by:
    #:
    #:  - ``COMMAND LIST``
    PATTERN = b"PATTERN"

    #: Used by:
    #:
    #:  - ``COPY``
    DB = b"DB"

    #: Used by:
    #:
    #:  - ``FAILOVER``
    TIMEOUT = b"TIMEOUT"

    #: Used by:
    #:
    #:  - ``FAILOVER``
    TO = b"TO"

    #: Used by:
    #:
    #:  - ``FUNCTION LIST``
    LIBRARYNAME = b"LIBRARYNAME"

    #: Used by:
    #:
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    #:  - ``SORT``
    STORE = b"STORE"

    #: Used by:
    #:
    #:  - ``GEORADIUS``
    #:  - ``GEORADIUSBYMEMBER``
    STOREDIST = b"STOREDIST"

    #: Used by:
    #:
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    BYBOX = b"BYBOX"

    #: Used by:
    #:
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    BYRADIUS = b"BYRADIUS"

    #: Used by:
    #:
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    FROMLONLAT = b"FROMLONLAT"

    #: Used by:
    #:
    #:  - ``GEOSEARCH``
    #:  - ``GEOSEARCHSTORE``
    FROMMEMBER = b"FROMMEMBER"

    #: Used by:
    #:
    #:  - ``GETEX``
    #:  - ``SET``
    EX = b"EX"

    #: Used by:
    #:
    #:  - ``GETEX``
    #:  - ``SET``
    EXAT = b"EXAT"

    #: Used by:
    #:
    #:  - ``GETEX``
    #:  - ``SET``
    PX = b"PX"

    #: Used by:
    #:
    #:  - ``GETEX``
    #:  - ``SET``
    PXAT = b"PXAT"

    #: Used by:
    #:
    #:  - ``HELLO``
    #:  - ``MIGRATE``
    AUTH = b"AUTH"

    #: Used by:
    #:
    #:  - ``HELLO``
    SETNAME = b"SETNAME"

    #: Used by:
    #:
    #:  - ``HSCAN``
    #:  - ``SCAN``
    #:  - ``SSCAN``
    #:  - ``ZSCAN``
    MATCH = b"MATCH"

    #: Used by:
    #:
    #:  - ``LCS``
    MINMATCHLEN = b"MINMATCHLEN"

    #: Used by:
    #:
    #:  - ``LOLWUT``
    VERSION = b"VERSION"

    #: Used by:
    #:
    #:  - ``LPOS``
    MAXLEN = b"MAXLEN"

    #: Used by:
    #:
    #:  - ``LPOS``
    RANK = b"RANK"

    #: Used by:
    #:
    #:  - ``MEMORY USAGE``
    SAMPLES = b"SAMPLES"

    #: Used by:
    #:
    #:  - ``MIGRATE``
    AUTH2 = b"AUTH2"

    #: Used by:
    #:
    #:  - ``MIGRATE``
    KEYS = b"KEYS"

    #: Used by:
    #:
    #:  - ``MODULE LOADEX``
    ARGS = b"ARGS"

    #: Used by:
    #:
    #:  - ``MODULE LOADEX``
    CONFIG = b"CONFIG"

    #: Used by:
    #:
    #:  - ``RESTORE``
    #:  - ``RESTORE-ASKING``
    FREQ = b"FREQ"

    #: Used by:
    #:
    #:  - ``RESTORE``
    #:  - ``RESTORE-ASKING``
    IDLETIME = b"IDLETIME"

    #: Used by:
    #:
    #:  - ``SINTERCARD``
    #:  - ``SORT``
    #:  - ``SORT_RO``
    #:  - ``XADD``
    #:  - ``XTRIM``
    #:  - ``ZINTERCARD``
    #:  - ``ZRANGE``
    #:  - ``ZRANGEBYLEX``
    #:  - ``ZRANGEBYSCORE``
    #:  - ``ZRANGESTORE``
    #:  - ``ZREVRANGEBYLEX``
    #:  - ``ZREVRANGEBYSCORE``
    LIMIT = b"LIMIT"

    #: Used by:
    #:
    #:  - ``SORT``
    #:  - ``SORT_RO``
    BY = b"BY"

    #: Used by:
    #:
    #:  - ``XCLAIM``
    #:  - ``XPENDING``
    IDLE = b"IDLE"

    #: Used by:
    #:
    #:  - ``XCLAIM``
    LASTID = b"LASTID"

    #: Used by:
    #:
    #:  - ``XCLAIM``
    RETRYCOUNT = b"RETRYCOUNT"

    #: Used by:
    #:
    #:  - ``XCLAIM``
    TIME = b"TIME"

    #: Used by:
    #:
    #:  - ``XGROUP CREATE``
    #:  - ``XGROUP SETID``
    ENTRIESREAD = b"ENTRIESREAD"

    #: Used by:
    #:
    #:  - ``XREAD``
    #:  - ``XREADGROUP``
    BLOCK = b"BLOCK"

    #: Used by:
    #:
    #:  - ``XREAD``
    #:  - ``XREADGROUP``
    STREAMS = b"STREAMS"

    #: Used by:
    #:
    #:  - ``XREADGROUP``
    GROUP = b"GROUP"

    #: Used by:
    #:
    #:  - ``XSETID``
    ENTRIESADDED = b"ENTRIESADDED"

    #: Used by:
    #:
    #:  - ``XSETID``
    MAXDELETEDID = b"MAXDELETEDID"

    #: Used by:
    #:
    #:  - ``ZINTER``
    #:  - ``ZINTERSTORE``
    #:  - ``ZUNION``
    #:  - ``ZUNIONSTORE``
    AGGREGATE = b"AGGREGATE"

    #: Used by:
    #:
    #:  - ``ZINTER``
    #:  - ``ZINTERSTORE``
    #:  - ``ZUNION``
    #:  - ``ZUNIONSTORE``
    WEIGHTS = b"WEIGHTS"

    #: Used by:
    #:
    #:  - ``JSON.GET``
    INDENT = b"INDENT"

    #: Used by:
    #:
    #:  - ``JSON.GET``
    NEWLINE = b"NEWLINE"

    #: Used by:
    #:
    #:  - ``JSON.GET``
    SPACE = b"SPACE"

    #: Used by:
    #:
    #:  - ``BF.INSERT``
    #:  - ``BF.RESERVE``
    #:  - ``CF.RESERVE``
    EXPANSION = b"EXPANSION"

    #: Used by:
    #:
    #:  - ``BF.INSERT``
    #:  - ``CF.INSERT``
    #:  - ``CF.INSERTNX``
    CAPACITY = b"CAPACITY"

    #: Used by:
    #:
    #:  - ``BF.INSERT``
    ERROR = b"ERROR"

    #: Used by:
    #:
    #:  - ``CF.RESERVE``
    BUCKETSIZE = b"BUCKETSIZE"

    #: Used by:
    #:
    #:  - ``CF.RESERVE``
    MAXITERATIONS = b"MAXITERATIONS"

    #: Used by:
    #:
    #:  - ``TDIGEST.CREATE``
    COMPRESSION = b"COMPRESSION"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    #:  - ``TS.DECRBY``
    #:  - ``TS.INCRBY``
    CHUNK_SIZE = b"CHUNK_SIZE"

    #: Used by:
    #:
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    DUPLICATE_POLICY = b"DUPLICATE_POLICY"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.CREATE``
    ENCODING = b"ENCODING"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    #:  - ``TS.DECRBY``
    #:  - ``TS.INCRBY``
    LABELS = b"LABELS"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    #:  - ``TS.ALTER``
    #:  - ``TS.CREATE``
    #:  - ``TS.DECRBY``
    #:  - ``TS.INCRBY``
    RETENTION = b"RETENTION"

    #: Used by:
    #:
    #:  - ``TS.ADD``
    ON_DUPLICATE = b"ON_DUPLICATE"

    #: Used by:
    #:
    #:  - ``TS.DECRBY``
    #:  - ``TS.INCRBY``
    TIMESTAMP = b"TIMESTAMP"

    #: Used by:
    #:
    #:  - ``TS.CREATERULE``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    AGGREGATION = b"AGGREGATION"

    #: Used by:
    #:
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    ALIGN = b"ALIGN"

    #: Used by:
    #:
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    #:  - ``TS.RANGE``
    #:  - ``TS.REVRANGE``
    FILTER_BY_TS = b"FILTER_BY_TS"

    #: Used by:
    #:
    #:  - ``TS.MGET``
    #:  - ``TS.MRANGE``
    #:  - ``TS.MREVRANGE``
    FILTER = b"FILTER"
