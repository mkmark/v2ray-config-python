from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext
# import v2ray_config.common.protofilter as protofilter
# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class implementationRegistry:
    implSet: Optional[dict[str, implementationSet]] = field(default_factory=dict[str, implementationSet])


@dataclass(slots=True)
class registerRequest:
    proto: Optional[dict] = field(default_factory=dict)
    loader: Optional[CustomLoader] = field(default_factory=CustomLoader)
