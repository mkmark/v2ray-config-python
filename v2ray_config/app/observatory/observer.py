from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.common.signal.done as done
# import v2ray_config.common.task as task
# import v2ray_config.features.extension as extension
# import v2ray_config.features.outbound as outbound
# import v2ray_config.transport.internet.tagged as tagged


@dataclass(slots=True)
class Observer:
    config: Optional[Config] = field(default_factory=Config)
    ctx: Optional[Context] = field(default_factory=Context)
    statusLock: Optional[Mutex] = field(default_factory=Mutex)
    status: Optional[list[OutboundStatus]] = field(default_factory=list[OutboundStatus])
    finished: Optional[Instance] = field(default_factory=Instance)
    ohm: Optional[Manager] = field(default_factory=Manager)
