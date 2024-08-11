from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net


@dataclass(slots=True)
class Config:
    address: Optional[str] = None
    port: Optional[int] = None
    network_list: Optional[list[str]] = field(default_factory=list[str])
    networks: Optional[list[str]] = field(default_factory=list[str])
    timeout: Optional[int] = None
    follow_redirect: Optional[bool] = None
    user_level: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
