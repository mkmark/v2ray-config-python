from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.dns as dns
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.strmatcher as strmatcher
# import v2ray_config.common.task as task
# import v2ray_config.features.dns as dns
# import v2ray_config.features.policy as policy
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet


# @dataclass(slots=True)
# class Handler:
#     client: Optional[Client] = field(default_factory=Client)
#     ipv_4_lookup: Optional[IPv4Lookup] = field(default_factory=IPv4Lookup)
#     ipv_6_lookup: Optional[IPv6Lookup] = field(default_factory=IPv6Lookup)
#     own_link_verifier: Optional[ownLinkVerifier] = field(default_factory=ownLinkVerifier)
#     server: Optional[Destination] = field(default_factory=Destination)
#     timeout: Optional[str] = None


# @dataclass(slots=True)
# class outboundConn:
#     access: Optional[Mutex] = field(default_factory=Mutex)
#     conn: Optional[Conn] = field(default_factory=Conn)
#     conn_ready: Optional[chan] = field(default_factory=chan)
