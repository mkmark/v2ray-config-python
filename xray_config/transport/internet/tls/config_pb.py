from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Certificate_Usage(int):
    pass


@dataclass(slots=True)
class Certificate:
    certificate: Optional[list[int]] = field(default_factory=list[int])
    key: Optional[list[int]] = field(default_factory=list[int])
    usage: Optional[Certificate_Usage] = field(default_factory=Certificate_Usage)
    ocsp_stapling: Optional[int] = None
    certificate_path: Optional[str] = None
    key_path: Optional[str] = None
    one_time_loading: Optional[bool] = None
    build_chain: Optional[bool] = None


@dataclass(slots=True)
class Config:
    allow_insecure: Optional[bool] = None
    certificate: Optional[list[Certificate]] = field(default_factory=list[Certificate])
    server_name: Optional[str] = None
    next_protocol: Optional[list[str]] = field(default_factory=list[str])
    enable_session_resumption: Optional[bool] = None
    disable_system_root: Optional[bool] = None
    min_version: Optional[str] = None
    max_version: Optional[str] = None
    cipher_suites: Optional[str] = None
    prefer_server_cipher_suites: Optional[bool] = None
    fingerprint: Optional[str] = None
    reject_unknown_sni: Optional[bool] = None
    pinned_peer_certificate_chain_sha256: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    pinned_peer_certificate_public_key_sha256: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    master_key_log: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
