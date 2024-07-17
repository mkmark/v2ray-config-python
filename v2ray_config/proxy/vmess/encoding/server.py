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


# @dataclass(slots=True)
# class sessionID:
#     user: Optional[[16]byte] = field(default_factory=[16]byte)
#     key: Optional[[16]byte] = field(default_factory=[16]byte)
#     nonce: Optional[[16]byte] = field(default_factory=[16]byte)


# @dataclass(slots=True)
# class SessionHistory(RWMutex):
#     cache: Optional[dict[sessionID, Time]] = field(default_factory=dict[sessionID, Time])
#     task: Optional[Periodic] = field(default_factory=Periodic)


# @dataclass(slots=True)
# class ServerSession:
#     user_validator: Optional[TimedUserValidator] = field(default_factory=TimedUserValidator)
#     session_history: Optional[SessionHistory] = field(default_factory=SessionHistory)
#     request_body_key: Optional[[16]byte] = field(default_factory=[16]byte)
#     request_body_iv: Optional[[16]byte] = field(default_factory=[16]byte)
#     response_body_key: Optional[[16]byte] = field(default_factory=[16]byte)
#     response_body_iv: Optional[[16]byte] = field(default_factory=[16]byte)
#     response_writer: Optional[Writer] = field(default_factory=Writer)
#     response_header: Optional[int] = None
#     is_aead_request: Optional[bool] = None
#     is_aead_forced: Optional[bool] = None
