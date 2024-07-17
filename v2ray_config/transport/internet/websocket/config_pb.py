from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Header:
    key: Optional[str] = None
    value: Optional[str] = None


@dataclass(slots=True)
class Config:
    path: Optional[str] = None
    header: Optional[list[Header]] = field(default_factory=list[Header])
    accept_proxy_protocol: Optional[bool] = None
    max_early_data: Optional[int] = None
    use_browser_forwarding: Optional[bool] = None
    early_data_header_name: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
