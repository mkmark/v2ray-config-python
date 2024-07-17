from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.platform.filesystem as filesystem
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class TLSCertConfig:
    certificate_file: Optional[str] = None
    certificate: Optional[list[str]] = field(default_factory=list[str])
    key_file: Optional[str] = None
    key: Optional[list[str]] = field(default_factory=list[str])
    usage: Optional[str] = None


@dataclass(slots=True)
class TLSConfig:
    allow_insecure: Optional[bool] = None
    certificates: Optional[list[TLSCertConfig]] = field(
        default_factory=list[TLSCertConfig]
    )
    server_name: Optional[str] = None
    alpn: Optional[list[str]] = field(default_factory=list[str])
    enable_session_resumption: Optional[bool] = None
    disable_system_root: Optional[bool] = None
    pinned_peer_certificate_chain_sha_256: Optional[list[str]] = field(
        default_factory=list[str]
    )
    verify_client_certificate: Optional[bool] = None
