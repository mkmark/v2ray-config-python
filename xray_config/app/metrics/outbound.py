from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.net.cnc as cnc
# import xray_config.common.signal.done as done
# import xray_config.transport as transport


@dataclass(slots=True)
class OutboundListener:
    buffer: Optional[chan] = field(default_factory=chan)
    done: Optional[Instance] = field(default_factory=Instance)


@dataclass(slots=True)
class Outbound:
    tag: Optional[str] = None
    listener: Optional[OutboundListener] = field(default_factory=OutboundListener)
    access: Optional[RWMutex] = field(default_factory=RWMutex)
    closed: Optional[bool] = None
