from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.bitmask as bitmask
# import v2ray_config.common.buf as buf
# import v2ray_config.common.crypto as crypto
# import v2ray_config.common.drain as drain
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.task as task
# import v2ray_config.proxy.vmess as vmess
# import v2ray_config.proxy.vmess.aead as aead


@dataclass(slots=True)
class sessionID:
    user: Optional[[16]byte] = field(default_factory=[16]byte)
    key: Optional[[16]byte] = field(default_factory=[16]byte)
    nonce: Optional[[16]byte] = field(default_factory=[16]byte)


@dataclass(slots=True)
class SessionHistory(RWMutex):
    cache: Optional[dict[sessionID, Time]] = field(default_factory=dict[sessionID, Time])
    task: Optional[Periodic] = field(default_factory=Periodic)


@dataclass(slots=True)
class ServerSession:
    userValidator: Optional[TimedUserValidator] = field(default_factory=TimedUserValidator)
    sessionHistory: Optional[SessionHistory] = field(default_factory=SessionHistory)
    requestBodyKey: Optional[[16]byte] = field(default_factory=[16]byte)
    requestBodyIV: Optional[[16]byte] = field(default_factory=[16]byte)
    responseBodyKey: Optional[[16]byte] = field(default_factory=[16]byte)
    responseBodyIV: Optional[[16]byte] = field(default_factory=[16]byte)
    responseWriter: Optional[Writer] = field(default_factory=Writer)
    responseHeader: Optional[int] = None
    isAEADRequest: Optional[bool] = None
    isAEADForced: Optional[bool] = None
