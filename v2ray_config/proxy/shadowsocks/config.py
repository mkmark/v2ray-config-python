from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.antireplay as antireplay
# import v2ray_config.common.buf as buf
# import v2ray_config.common.crypto as crypto
# import v2ray_config.common.protocol as protocol


# @dataclass(slots=True)
# class MemoryAccount:
#     cipher: Optional[Cipher] = field(default_factory=Cipher)
#     key: Optional[list[int]] = field(default_factory=list[int])
#     replay_filter: Optional[GeneralizedReplayFilter] = field(default_factory=GeneralizedReplayFilter)
#     reduced_iv_entropy: Optional[bool] = None


@dataclass(slots=True)
class AEADCipher:
    key_bytes: Optional[int] = None
    iv_bytes: Optional[int] = None


@dataclass(slots=True)
class NoneCipher:
    pass
