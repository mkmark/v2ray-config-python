from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class FileLocker:
    path: Optional[str] = None
    file: Optional[File] = field(default_factory=File)
