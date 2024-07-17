from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class ClientConfig:
    http: Optional[HTTPConfig] = field(default_factory=HTTPConfig)


@dataclass(slots=True)
class ServerConfig:
    http: Optional[HTTPConfig] = field(default_factory=HTTPConfig)
    no_decoding_session_tag: Optional[bool] = None


@dataclass(slots=True)
class HTTPConfig:
    path: Optional[str] = None
    url_prefix: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
