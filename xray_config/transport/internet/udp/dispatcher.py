from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol.udp as udp
# import xray_config.common.signal as signal
# import xray_config.common.signal.done as done
# import xray_config.features.routing as routing
# import xray_config.transport as transport


@dataclass(slots=True)
class ResponseCallback(Packet)):
    pass


@dataclass(slots=True)
class connEntry:
    link: Optional[Link] = field(default_factory=Link)
    timer: Optional[ActivityUpdater] = field(default_factory=ActivityUpdater)
    cancel: Optional[CancelFunc] = field(default_factory=CancelFunc)


@dataclass(slots=True)
class Dispatcher(RWMutex):
    conn: Optional[connEntry] = field(default_factory=connEntry)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    callback: Optional[ResponseCallback] = field(default_factory=ResponseCallback)


@dataclass(slots=True)
class dispatcherConn:
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    cache: Optional[chan] = field(default_factory=chan)
    done: Optional[Instance] = field(default_factory=Instance)
    ctx: Optional[Context] = field(default_factory=Context)
