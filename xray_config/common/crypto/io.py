from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf


@dataclass(slots=True)
class CryptionReader:
    stream: Optional[Stream] = field(default_factory=Stream)
    reader: Optional[Reader] = field(default_factory=Reader)


@dataclass(slots=True)
class CryptionWriter:
    stream: Optional[Stream] = field(default_factory=Stream)
    writer: Optional[Writer] = field(default_factory=Writer)
    bufWriter: Optional[Writer] = field(default_factory=Writer)
