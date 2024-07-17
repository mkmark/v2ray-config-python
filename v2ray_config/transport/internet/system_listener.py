from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.session as session


@dataclass(slots=True)
class controller(func(network, address string, fd uintptr) error):
    pass


@dataclass(slots=True)
class DefaultListener:
    controllers: Optional[list[controller]] = field(default_factory=list[controller])


@dataclass(slots=True)
class combinedListener(Listener):
    locker: Optional[FileLocker] = field(default_factory=FileLocker)
