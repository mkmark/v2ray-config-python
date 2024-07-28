from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tls as tls
# import v2ray_config.transport.internet.udp as udp


@dataclass(slots=True)
class ConnectionID:
    remote: Optional[str] = None
    port: Optional[int] = None
    conv: Optional[int] = None


@dataclass(slots=True)
class Listener(Mutex):
    sessions: Optional[dict[ConnectionID, Connection]] = field(default_factory=dict[ConnectionID, Connection])
    hub: Optional[Hub] = field(default_factory=Hub)
    tlsConfig: Optional[Config] = field(default_factory=Config)
    config: Optional[Config] = field(default_factory=Config)
    reader: Optional[PacketReader] = field(default_factory=PacketReader)
    header: Optional[PacketHeader] = field(default_factory=PacketHeader)
    security: Optional[AEAD] = field(default_factory=AEAD)
    addConn: Optional[ConnHandler] = field(default_factory=ConnHandler)


@dataclass(slots=True)
class Writer:
    id: Optional[ConnectionID] = field(default_factory=ConnectionID)
    dest: Optional[Destination] = field(default_factory=Destination)
    hub: Optional[Hub] = field(default_factory=Hub)
    listener: Optional[Listener] = field(default_factory=Listener)
