from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol.tls.cert as cert
# import xray_config.common.signal.done as done
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Listener:
    rawConn: Optional[sysConn] = field(default_factory=sysConn)
    listener: Optional[Listener] = field(default_factory=Listener)
    done: Optional[Instance] = field(default_factory=Instance)
    addConn: Optional[ConnHandler] = field(default_factory=ConnHandler)
