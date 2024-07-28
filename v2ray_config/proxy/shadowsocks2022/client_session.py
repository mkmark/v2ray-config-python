from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class ClientUDPSession:
    locker: Optional[RWMutex] = field(default_factory=RWMutex)
    conn: Optional[ReadWriteCloser] = field(default_factory=ReadWriteCloser)
    packetProcessor: Optional[UDPClientPacketProcessor] = field(default_factory=UDPClientPacketProcessor)
    sessionMap: Optional[dict[str, ClientUDPSessionConn]] = field(default_factory=dict[str, ClientUDPSessionConn])
    sessionMapAlias: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class ClientUDPSessionServerTracker:
    cachedRecvProcessorState: Optional[UDPClientPacketProcessorCachedState] = field(default_factory=UDPClientPacketProcessorCachedState)
    rxReplayDetector: Optional[ReplayDetector] = field(default_factory=ReplayDetector)
    lastSeen: Optional[Time] = field(default_factory=Time)


@dataclass(slots=True)
class ClientUDPSessionConn:
    sessionID: Optional[str] = None
    readChan: Optional[chan] = field(default_factory=chan)
    parent: Optional[ClientUDPSession] = field(default_factory=ClientUDPSession)
    nextWritePacketID: Optional[int] = None
    trackedServerSessionID: Optional[dict[str, ClientUDPSessionServerTracker]] = field(default_factory=dict[str, ClientUDPSessionServerTracker])
    cachedProcessorState: Optional[UDPClientPacketProcessorCachedState] = field(default_factory=UDPClientPacketProcessorCachedState)
    ctx: Optional[Context] = field(default_factory=Context)
