from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.infra.conf.cfgcommon as cfgcommon


@dataclass(slots=True)
class SniffingConfig:
    enabled: Optional[bool] = None
    destOverride: Optional[list[str]] = field(default_factory=list[str])
    metadataOnly: Optional[bool] = None
