from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol.dns as dns
# import xray_config.common.session as session
# import xray_config.common.signal as signal
# import xray_config.common.task as task
# import xray_config.core as core
# import xray_config.features.dns as dns
# import xray_config.features.policy as policy
# import xray_config.transport as transport
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.stat as stat


@dataclass(slots=True)
class Handler:
    client: Optional[Client] = field(default_factory=Client)
    fdns: Optional[FakeDNSEngine] = field(default_factory=FakeDNSEngine)
    ownLinkVerifier: Optional[ownLinkVerifier] = field(default_factory=ownLinkVerifier)
    server: Optional[Destination] = field(default_factory=Destination)
    timeout: Optional[str] = None
    nonIPQuery: Optional[str] = None


@dataclass(slots=True)
class outboundConn:
    access: Optional[Mutex] = field(default_factory=Mutex)
    conn: Optional[Conn] = field(default_factory=Conn)
    connReady: Optional[chan] = field(default_factory=chan)
