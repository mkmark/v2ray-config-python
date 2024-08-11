from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.commander as commander
# import xray_config.app.log.command as command
# import xray_config.app.observatory.command as command
# import xray_config.app.proxyman.command as command
# import xray_config.app.router.command as command
# import xray_config.app.stats.command as command
# import xray_config.common.errors as errors
# import xray_config.common.serial as serial


@dataclass(slots=True)
class APIConfig:
    tag: Optional[str] = None
    listen: Optional[str] = None
    services: Optional[list[str]] = field(default_factory=list[str])
