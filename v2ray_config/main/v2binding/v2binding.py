from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.commander as commander
# import v2ray_config.app.dispatcher as dispatcher
# import v2ray_config.app.instman as instman
# import v2ray_config.app.instman.command as command
# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.app.router as router
# import v2ray_config.common.net as net
# import v2ray_config.common.serial as serial
# import v2ray_config.main.distro.all as all
# import v2ray_config.proxy.blackhole as blackhole
# import v2ray_config.proxy.dokodemo as dokodemo


@dataclass(slots=True)
class bindingInstance:
    started: Optional[bool] = None
    instance: Optional[Instance] = field(default_factory=Instance)
