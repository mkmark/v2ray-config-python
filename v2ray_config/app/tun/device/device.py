from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common


@dataclass(slots=True)
class DeviceConstructor(func(Options) (Device, error)):
    pass


@dataclass(slots=True)
class Options:
    name: Optional[str] = None
    mTU: Optional[int] = None
