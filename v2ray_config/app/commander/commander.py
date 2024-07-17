from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.serial as serial
# import v2ray_config.common.signal.done as done
# import v2ray_config.features.outbound as outbound
# import v2ray_config.infra.conf.v5cfg as v5cfg


@dataclass(slots=True)
class Commander(Mutex):
    server: Optional[Server] = field(default_factory=Server)
    services: Optional[list[Service]] = field(default_factory=list[Service])
    ohm: Optional[Manager] = field(default_factory=Manager)
    tag: Optional[str] = None
