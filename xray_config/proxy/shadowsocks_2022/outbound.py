from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.session as session
# import xray_config.common.singbridge as singbridge
# import xray_config.transport as transport
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class Outbound:
    ctx: Optional[Context] = field(default_factory=Context)
    server: Optional[Destination] = field(default_factory=Destination)
    method: Optional[Method] = field(default_factory=Method)
    uotClient: Optional[Client] = field(default_factory=Client)
