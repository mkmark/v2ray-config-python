from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.udp as udp
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.signal.done as done
# import v2ray_config.features.routing as routing
# import v2ray_config.transport as transport


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
    conns: Optional[dict[Destination, connEntry]] = field(default_factory=dict[Destination, connEntry])
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    callback: Optional[ResponseCallback] = field(default_factory=ResponseCallback)


@dataclass(slots=True)
class dispatcherConn:
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    cache: Optional[chan] = field(default_factory=chan)
    done: Optional[Instance] = field(default_factory=Instance)
