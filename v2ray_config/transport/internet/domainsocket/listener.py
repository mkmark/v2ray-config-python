from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Listener:
    addr: Optional[UnixAddr] = field(default_factory=UnixAddr)
    ln: Optional[Listener] = field(default_factory=Listener)
    tls_config: Optional[Config] = field(default_factory=Config)
    config: Optional[Config] = field(default_factory=Config)
    add_conn: Optional[ConnHandler] = field(default_factory=ConnHandler)
    locker: Optional[fileLocker] = field(default_factory=fileLocker)


@dataclass(slots=True)
class fileLocker:
    path: Optional[str] = None
    file: Optional[File] = field(default_factory=File)
