from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.antireplay as antireplay
# import xray_config.common.buf as buf
# import xray_config.common.crypto as crypto
# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class MemoryAccount:
    cipher: Optional[Cipher] = field(default_factory=Cipher)
    key: Optional[list[int]] = field(default_factory=list[int])
    replayFilter: Optional[GeneralizedReplayFilter] = field(default_factory=GeneralizedReplayFilter)


@dataclass(slots=True)
class AEADCipher:
    keyBytes: Optional[int] = None
    iVBytes: Optional[int] = None


@dataclass(slots=True)
class NoneCipher:
    pass
