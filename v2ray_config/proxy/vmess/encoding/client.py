from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.bitmask as bitmask
# import v2ray_config.common.buf as buf
# import v2ray_config.common.crypto as crypto
# import v2ray_config.common.dice as dice
# import v2ray_config.common.drain as drain
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial
# import v2ray_config.proxy.vmess as vmess
# import v2ray_config.proxy.vmess.aead as aead


# @dataclass(slots=True)
# class ClientSession:
#     is_aead: Optional[bool] = None
#     id_hash: Optional[IDHash] = field(default_factory=IDHash)
#     request_body_key: Optional[[16]byte] = field(default_factory=[16]byte)
#     request_body_iv: Optional[[16]byte] = field(default_factory=[16]byte)
#     response_body_key: Optional[[16]byte] = field(default_factory=[16]byte)
#     response_body_iv: Optional[[16]byte] = field(default_factory=[16]byte)
#     response_reader: Optional[Reader] = field(default_factory=Reader)
#     response_header: Optional[int] = None
#     read_drainer: Optional[Drainer] = field(default_factory=Drainer)
