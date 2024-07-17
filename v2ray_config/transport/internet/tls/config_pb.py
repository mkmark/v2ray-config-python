from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Certificate_Usage(int):
    pass


@dataclass(slots=True)
class Config_TLSVersion(int):
    pass


@dataclass(slots=True)
class Certificate:
    Certificate: Optional[str] = None
    Key: Optional[str] = None
    usage: Optional[Certificate_Usage] = field(default_factory=Certificate_Usage)
    certificate_file: Optional[str] = None
    key_file: Optional[str] = None


@dataclass(slots=True)
class Config:
    allow_insecure: Optional[bool] = None
    certificate: Optional[list[Certificate]] = field(default_factory=list[Certificate])
    server_name: Optional[str] = None
    next_protocol: Optional[list[str]] = field(default_factory=list[str])
    enable_session_resumption: Optional[bool] = None
    disable_system_root: Optional[bool] = None
    pinned_peer_certificate_chain_sha_256: Optional[list[list[int]]] = field(
        default_factory=list[list[int]]
    )
    verify_client_certificate: Optional[bool] = None
    min_version: Optional[Config_TLSVersion] = field(default_factory=Config_TLSVersion)
    max_version: Optional[Config_TLSVersion] = field(default_factory=Config_TLSVersion)


@dataclass(slots=True)
class x:
    pass
