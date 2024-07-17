from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.proxy.dokodemo as dokodemo


@dataclass(slots=True)
class DokodemoConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    network: Optional[list[str]] = field(default_factory=list[str])
    timeout: Optional[int] = None
    follow_redirect: Optional[bool] = None
    user_level: Optional[int] = None
