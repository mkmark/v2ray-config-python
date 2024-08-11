from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net
# import xray_config.common.session as session
# import xray_config.features.routing as routing


@dataclass(slots=True)
class Context:
    inbound: Optional[Inbound] = field(default_factory=Inbound)
    outbound: Optional[Outbound] = field(default_factory=Outbound)
    content: Optional[Content] = field(default_factory=Content)
