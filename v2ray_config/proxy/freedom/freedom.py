from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.dice as dice
# import v2ray_config.common.net as net
# import v2ray_config.common.retry as retry
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.task as task
# import v2ray_config.features.dns as dns
# import v2ray_config.features.policy as policy
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class Handler:
    policyManager: Optional[Manager] = field(default_factory=Manager)
    dns: Optional[Client] = field(default_factory=Client)
    config: Optional[Config] = field(default_factory=Config)
