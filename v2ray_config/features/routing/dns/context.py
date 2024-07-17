from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.features.dns as dns
# import v2ray_config.features.routing as routing


@dataclass(slots=True)
class ResolvableContext(Context):
    dns_client: Optional[Client] = field(default_factory=Client)
    resolved_i_ps: Optional[list[IP]] = field(default_factory=list[IP])
