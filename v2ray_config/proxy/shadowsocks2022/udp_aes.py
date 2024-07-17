from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net


# @dataclass(slots=True)
# class AESUDPClientPacketProcessor:
#     request_separate_header_block_cipher: Optional[Block] = field(default_factory=Block)
#     response_separate_header_block_cipher: Optional[Block] = field(default_factory=Block)


# @dataclass(slots=True)
# class separateHeader:
#     session_id: Optional[[8]byte] = field(default_factory=[8]byte)
#     packet_id: Optional[int] = None


# @dataclass(slots=True)
# class header:
#     type: Optional[int] = None
#     time_stamp: Optional[int] = None
#     padding_length: Optional[int] = None
#     padding: Optional[list[int]] = field(default_factory=list[int])


# @dataclass(slots=True)
# class respHeader:
#     type: Optional[int] = None
#     time_stamp: Optional[int] = None
#     client_session_id: Optional[[8]byte] = field(default_factory=[8]byte)
#     padding_length: Optional[int] = None
#     padding: Optional[list[int]] = field(default_factory=list[int])


# @dataclass(slots=True)
# class cachedUDPState:
#     session_aead: Optional[AEAD] = field(default_factory=AEAD)
#     session_recv_aead: Optional[AEAD] = field(default_factory=AEAD)
