from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.tls.cert as cert
# import v2ray_config.common.signal.done as done
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Listener:
    raw_conn: Optional[sysConn] = field(default_factory=sysConn)
    listener: Optional[Listener] = field(default_factory=Listener)
    done: Optional[Instance] = field(default_factory=Instance)
    add_conn: Optional[ConnHandler] = field(default_factory=ConnHandler)
