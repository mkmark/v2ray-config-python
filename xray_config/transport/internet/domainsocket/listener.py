from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.reality as reality
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Listener:
    addr: Optional[UnixAddr] = field(default_factory=UnixAddr)
    ln: Optional[Listener] = field(default_factory=Listener)
    tlsConfig: Optional[Config] = field(default_factory=Config)
    realityConfig: Optional[Config] = field(default_factory=Config)
    config: Optional[Config] = field(default_factory=Config)
    addConn: Optional[ConnHandler] = field(default_factory=ConnHandler)
    locker: Optional[fileLocker] = field(default_factory=fileLocker)


@dataclass(slots=True)
class fileLocker:
    path: Optional[str] = None
    file: Optional[File] = field(default_factory=File)
