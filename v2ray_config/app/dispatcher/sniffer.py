from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.bittorrent as bittorrent
# import v2ray_config.common.protocol.http as http
# import v2ray_config.common.protocol.quic as quic
# import v2ray_config.common.protocol.tls as tls


@dataclass(slots=True)
class protocolSniffer(Context, []byte) (SniffResult, error)):
    pass


@dataclass(slots=True)
class protocolSnifferWithMetadata:
    protocolSniffer: Optional[protocolSniffer] = field(default_factory=protocolSniffer)
    metadataSniffer: Optional[bool] = None
    network: Optional[str] = None


@dataclass(slots=True)
class Sniffer:
    sniffer: Optional[list[protocolSnifferWithMetadata]] = field(default_factory=list[protocolSnifferWithMetadata])


@dataclass(slots=True)
class compositeResult:
    domainResult: Optional[SniffResult] = field(default_factory=SniffResult)
    protocolResult: Optional[SniffResult] = field(default_factory=SniffResult)
