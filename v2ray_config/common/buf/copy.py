from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.errors as errors
# import v2ray_config.common.signal as signal


@dataclass(slots=True)
class dataHandler(func(MultiBuffer)):
    pass


@dataclass(slots=True)
class CopyOption(func(*copyHandler)):
    pass


@dataclass(slots=True)
class copyHandler:
    onData: Optional[list[dataHandler]] = field(default_factory=list[dataHandler])


@dataclass(slots=True)
class SizeCounter:
    size: Optional[int] = None


@dataclass(slots=True)
class readError(error):
    pass


@dataclass(slots=True)
class writeError(error):
    pass
