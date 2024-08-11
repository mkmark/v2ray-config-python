from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol.http as http
# import xray_config.common.signal.done as done
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class requestHandler:
    config: Optional[Config] = field(default_factory=Config)
    host: Optional[str] = None
    path: Optional[str] = None
    ln: Optional[Listener] = field(default_factory=Listener)
    sessionMu: Optional[Mutex] = field(default_factory=Mutex)
    sessions: Optional[Map] = field(default_factory=Map)
    localAddr: Optional[TCPAddr] = field(default_factory=TCPAddr)


@dataclass(slots=True)
class httpSession:
    uploadQueue: Optional[uploadQueue] = field(default_factory=uploadQueue)
    isFullyConnected: Optional[Instance] = field(default_factory=Instance)


@dataclass(slots=True)
class httpResponseBodyWriter(Mutex):
    responseWriter: Optional[ResponseWriter] = field(default_factory=ResponseWriter)
    responseFlusher: Optional[Flusher] = field(default_factory=Flusher)
    downloadDone: Optional[Instance] = field(default_factory=Instance)


@dataclass(slots=True)
class Listener(Mutex):
    server: Optional[Server] = field(default_factory=Server)
    h3server: Optional[Server] = field(default_factory=Server)
    listener: Optional[Listener] = field(default_factory=Listener)
    h3listener: Optional[EarlyListener] = field(default_factory=EarlyListener)
    config: Optional[Config] = field(default_factory=Config)
    addConn: Optional[ConnHandler] = field(default_factory=ConnHandler)
    isH3: Optional[bool] = None
