from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.crypto as crypto


@dataclass(slots=True)
class NoOpAuthenticator:
    pass


@dataclass(slots=True)
class FnvAuthenticator:
    pass


# @dataclass(slots=True)
# class ShakeSizeParser:
#     shake: Optional[ShakeHash] = field(default_factory=ShakeHash)
#     buffer: Optional[[2]byte] = field(default_factory=[2]byte)


# @dataclass(slots=True)
# class AEADSizeParser(AEADChunkSizeParser):
#     pass
