from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.bytespool as bytespool
# import v2ray_config.common.errors as errors
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class BytesGenerator(func() []byte):
    pass


@dataclass(slots=True)
class AEADAuthenticator(AEAD):
    nonceGenerator: Optional[BytesGenerator] = field(default_factory=BytesGenerator)
    additionalDataGenerator: Optional[BytesGenerator] = field(default_factory=BytesGenerator)


@dataclass(slots=True)
class AuthenticationReader:
    auth: Optional[Authenticator] = field(default_factory=Authenticator)
    reader: Optional[BufferedReader] = field(default_factory=BufferedReader)
    sizeParser: Optional[ChunkSizeDecoder] = field(default_factory=ChunkSizeDecoder)
    sizeBytes: Optional[list[int]] = field(default_factory=list[int])
    transferType: Optional[TransferType] = field(default_factory=TransferType)
    padding: Optional[PaddingLengthGenerator] = field(default_factory=PaddingLengthGenerator)
    size: Optional[int] = None
    sizeOffset: Optional[int] = None
    paddingLen: Optional[int] = None
    hasSize: Optional[bool] = None
    done: Optional[bool] = None


@dataclass(slots=True)
class AuthenticationWriter:
    auth: Optional[Authenticator] = field(default_factory=Authenticator)
    writer: Optional[Writer] = field(default_factory=Writer)
    sizeParser: Optional[ChunkSizeEncoder] = field(default_factory=ChunkSizeEncoder)
    transferType: Optional[TransferType] = field(default_factory=TransferType)
    padding: Optional[PaddingLengthGenerator] = field(default_factory=PaddingLengthGenerator)
