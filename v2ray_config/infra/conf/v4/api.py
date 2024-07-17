from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.commander as commander
# import v2ray_config.app.log.command as command
# import v2ray_config.app.observatory.command as command
# import v2ray_config.app.proxyman.command as command
# import v2ray_config.app.router.command as command
# import v2ray_config.app.stats.command as command
# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class APIConfig:
    tag: Optional[str] = None
    services: Optional[list[str]] = field(default_factory=list[str])
