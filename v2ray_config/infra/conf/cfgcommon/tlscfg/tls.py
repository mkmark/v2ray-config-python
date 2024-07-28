from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.platform.filesystem as filesystem
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class TLSCertConfig:
    certificateFile: Optional[str] = None
    certificate: Optional[list[str]] = field(default_factory=list[str])
    keyFile: Optional[str] = None
    key: Optional[list[str]] = field(default_factory=list[str])
    usage: Optional[str] = None


@dataclass(slots=True)
class TLSConfig:
    allowInsecure: Optional[bool] = None
    certificates: Optional[list[TLSCertConfig]] = field(
        default_factory=list[TLSCertConfig]
    )
    serverName: Optional[str] = None
    alpn: Optional[list[str]] = field(default_factory=list[str])
    enableSessionResumption: Optional[bool] = None
    disableSystemRoot: Optional[bool] = None
    pinnedPeerCertificateChainSha256: Optional[list[str]] = field(
        default_factory=list[str]
    )
    verifyClientCertificate: Optional[bool] = None
