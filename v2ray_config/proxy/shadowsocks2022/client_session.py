from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.transport.internet as internet


# @dataclass(slots=True)
# class ClientUDPSession:
#     locker: Optional[RWMutex] = field(default_factory=RWMutex)
#     conn: Optional[ReadWriteCloser] = field(default_factory=ReadWriteCloser)
#     packet_processor: Optional[UDPClientPacketProcessor] = field(default_factory=UDPClientPacketProcessor)
#     session_map: Optional[dict[str, ClientUDPSessionConn]] = field(default_factory=dict[str, ClientUDPSessionConn])
#     session_map_alias: Optional[dict[str, str]] = field(default_factory=dict[str, str])
#     ctx: Optional[Context] = field(default_factory=Context)


# @dataclass(slots=True)
# class ClientUDPSessionServerTracker:
#     cached_recv_processor_state: Optional[UDPClientPacketProcessorCachedState] = field(default_factory=UDPClientPacketProcessorCachedState)
#     rx_replay_detector: Optional[ReplayDetector] = field(default_factory=ReplayDetector)
#     last_seen: Optional[Time] = field(default_factory=Time)


# @dataclass(slots=True)
# class ClientUDPSessionConn:
#     session_id: Optional[str] = None
#     read_chan: Optional[chan] = field(default_factory=chan)
#     parent: Optional[ClientUDPSession] = field(default_factory=ClientUDPSession)
#     next_write_packet_id: Optional[int] = None
#     tracked_server_session_id: Optional[dict[str, ClientUDPSessionServerTracker]] = field(default_factory=dict[str, ClientUDPSessionServerTracker])
#     cached_processor_state: Optional[UDPClientPacketProcessorCachedState] = field(default_factory=UDPClientPacketProcessorCachedState)
#     ctx: Optional[Context] = field(default_factory=Context)
