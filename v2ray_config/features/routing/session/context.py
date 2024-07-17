from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.features.routing as routing


@dataclass(slots=True)
class Context:
    inbound: Optional[Inbound] = field(default_factory=Inbound)
    outbound: Optional[Outbound] = field(default_factory=Outbound)
    content: Optional[Content] = field(default_factory=Content)
