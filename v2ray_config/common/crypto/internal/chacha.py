from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class ChaCha20Stream:
    block: Optional[[blockSize]byte] = field(default_factory=[blockSize]byte)
    offset: Optional[int] = None
    rounds: Optional[int] = None
