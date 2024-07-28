from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net


@dataclass(slots=True)
class AESUDPClientPacketProcessor:
    requestSeparateHeaderBlockCipher: Optional[Block] = field(default_factory=Block)
    responseSeparateHeaderBlockCipher: Optional[Block] = field(default_factory=Block)


@dataclass(slots=True)
class separateHeader:
    sessionID: Optional[[8]byte] = field(default_factory=[8]byte)
    packetID: Optional[int] = None


@dataclass(slots=True)
class header:
    type: Optional[int] = None
    timeStamp: Optional[int] = None
    paddingLength: Optional[int] = None
    padding: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class respHeader:
    type: Optional[int] = None
    timeStamp: Optional[int] = None
    clientSessionID: Optional[[8]byte] = field(default_factory=[8]byte)
    paddingLength: Optional[int] = None
    padding: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class cachedUDPState:
    sessionAEAD: Optional[AEAD] = field(default_factory=AEAD)
    sessionRecvAEAD: Optional[AEAD] = field(default_factory=AEAD)
