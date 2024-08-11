from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.serial as serial


@dataclass(slots=True)
class Config:
    header_settings: Optional[dict] = field(default_factory=dict)
    accept_proxy_protocol: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
