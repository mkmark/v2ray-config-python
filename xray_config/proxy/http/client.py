from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.bytespool as bytespool
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.retry as retry
# import xray_config.common.session as session
# import xray_config.common.signal as signal
# import xray_config.common.task as task
# import xray_config.core as core
# import xray_config.features.policy as policy
# import xray_config.transport as transport
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Client:
    serverPicker: Optional[ServerPicker] = field(default_factory=ServerPicker)
    policyManager: Optional[Manager] = field(default_factory=Manager)
    header: Optional[list[Header]] = field(default_factory=list[Header])


@dataclass(slots=True)
class h2Conn:
    rawConn: Optional[Conn] = field(default_factory=Conn)
    h2Conn: Optional[ClientConn] = field(default_factory=ClientConn)


@dataclass(slots=True)
class http2Conn(Conn):
    in: Optional[PipeWriter] = field(default_factory=PipeWriter)
    out: Optional[ReadCloser] = field(default_factory=ReadCloser)
