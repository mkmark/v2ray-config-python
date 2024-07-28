from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf


@dataclass(slots=True)
class aesEIH:
    eih: Optional[list[[aesEIHSize]byte]] = field(default_factory=list[[aesEIHSize]byte])
    length: Optional[int] = None


@dataclass(slots=True)
class aesEIHGenerator:
    ipsk: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    ipskHash: Optional[list[[aesEIHPskHashSize]byte]] = field(default_factory=list[[aesEIHPskHashSize]byte])
    psk: Optional[list[int]] = field(default_factory=list[int])
    pskHash: Optional[[aesEIHPskHashSize]byte] = field(default_factory=[aesEIHPskHashSize]byte)
    length: Optional[int] = None
