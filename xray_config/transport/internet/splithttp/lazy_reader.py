from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors


@dataclass(slots=True)
class LazyReader:
    readerSync: Optional[Mutex] = field(default_factory=Mutex)
    reader: Optional[ReadCloser] = field(default_factory=ReadCloser)
    readerError: Optional[error] = field(default_factory=error)
