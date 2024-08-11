from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.dispatcher as dispatcher
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.session as session
# import xray_config.common.signal as signal
# import xray_config.features.routing as routing
# import xray_config.features.stats as stats
# import xray_config.transport as transport
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.reality as reality
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class TrafficState:
    userUUID: Optional[list[int]] = field(default_factory=list[int])
    numberOfPacketToFilter: Optional[int] = None
    enableXtls: Optional[bool] = None
    isTLS12orAbove: Optional[bool] = None
    isTLS: Optional[bool] = None
    cipher: Optional[int] = None
    remainingServerHello: Optional[int] = None
    withinPaddingBuffers: Optional[bool] = None
    readerSwitchToDirectCopy: Optional[bool] = None
    remainingCommand: Optional[int] = None
    remainingContent: Optional[int] = None
    remainingPadding: Optional[int] = None
    currentCommand: Optional[int] = None
    isPadding: Optional[bool] = None
    writerSwitchToDirectCopy: Optional[bool] = None


@dataclass(slots=True)
class VisionReader(Reader):
    trafficState: Optional[TrafficState] = field(default_factory=TrafficState)
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class VisionWriter(Writer):
    trafficState: Optional[TrafficState] = field(default_factory=TrafficState)
    ctx: Optional[Context] = field(default_factory=Context)
    writeOnceUserUUID: Optional[list[int]] = field(default_factory=list[int])
