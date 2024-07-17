from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.features.dns as dns
# import v2ray_config.features.dns.localdns as localdns


@dataclass(slots=True)
class LocalNameServer:
    client: Optional[Client] = field(default_factory=Client)
