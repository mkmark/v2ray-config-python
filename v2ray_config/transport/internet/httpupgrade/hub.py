from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.transportcommon as transportcommon


@dataclass(slots=True)
class server:
    add_conn: Optional[ConnHandler] = field(default_factory=ConnHandler)
    innner_listener: Optional[Listener] = field(default_factory=Listener)
