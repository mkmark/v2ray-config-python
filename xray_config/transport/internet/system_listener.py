from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net


@dataclass(slots=True)
class DefaultListener:
    controllers: Optional[list[Func]] = field(default_factory=list[Func])


@dataclass(slots=True)
class combinedListener(Listener):
    locker: Optional[FileLocker] = field(default_factory=FileLocker)
