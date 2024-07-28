from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.crypto as crypto
# import v2ray_config.common.dice as dice
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class TCPRequest:
    keyDerivation: Optional[KeyDerivation] = field(default_factory=KeyDerivation)
    method: Optional[Method] = field(default_factory=Method)
    c2sSalt: Optional[RequestSalt] = field(default_factory=RequestSalt)
    c2sNonce: Optional[BytesGenerator] = field(default_factory=BytesGenerator)
    c2sAEAD: Optional[AEAD] = field(default_factory=AEAD)
    s2cSalt: Optional[RequestSalt] = field(default_factory=RequestSalt)
    s2cNonce: Optional[BytesGenerator] = field(default_factory=BytesGenerator)
    s2cAEAD: Optional[AEAD] = field(default_factory=AEAD)
    s2cSaltAssert: Optional[RequestSalt] = field(default_factory=RequestSalt)
    s2cInitialPayloadSize: Optional[int] = None


@dataclass(slots=True)
class AEADChunkSizeParser:
    auth: Optional[AEADAuthenticator] = field(default_factory=AEADAuthenticator)
