from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class ClientConfig:
    max_write_size: Optional[int] = None
    wait_subsequent_write_ms: Optional[int] = None
    initial_polling_interval_ms: Optional[int] = None
    max_polling_interval_ms: Optional[int] = None
    min_polling_interval_ms: Optional[int] = None
    backoff_factor: Optional[float] = None
    failed_retry_interval_ms: Optional[int] = None


@dataclass(slots=True)
class ServerConfig:
    max_write_size: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
