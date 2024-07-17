from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.crypto as crypto
# import v2ray_config.common.dice as dice
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol


# @dataclass(slots=True)
# class TCPRequest:
#     key_derivation: Optional[KeyDerivation] = field(default_factory=KeyDerivation)
#     method: Optional[Method] = field(default_factory=Method)
#     c_2s_salt: Optional[RequestSalt] = field(default_factory=RequestSalt)
#     c_2s_nonce: Optional[BytesGenerator] = field(default_factory=BytesGenerator)
#     c_2s_aead: Optional[AEAD] = field(default_factory=AEAD)
#     s_2c_salt: Optional[RequestSalt] = field(default_factory=RequestSalt)
#     s_2c_nonce: Optional[BytesGenerator] = field(default_factory=BytesGenerator)
#     s_2c_aead: Optional[AEAD] = field(default_factory=AEAD)
#     s_2c_salt_assert: Optional[RequestSalt] = field(default_factory=RequestSalt)
#     s_2c_initial_payload_size: Optional[int] = None


# @dataclass(slots=True)
# class AEADChunkSizeParser:
#     auth: Optional[AEADAuthenticator] = field(default_factory=AEADAuthenticator)
