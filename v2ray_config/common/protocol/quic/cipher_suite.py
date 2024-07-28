from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class cipherSuiteTLS13:
    iD: Optional[int] = None
    keyLen: Optional[int] = None
    hash: Optional[Hash] = field(default_factory=Hash)
