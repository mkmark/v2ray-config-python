from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.features.dns as dns
# import v2ray_config.features.routing as routing


@dataclass(slots=True)
class ResolvableContext(Context):
    dnsClient: Optional[Client] = field(default_factory=Client)
    resolvedIPs: Optional[list[IP]] = field(default_factory=list[IP])
