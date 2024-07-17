from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext
# import v2ray_config.common.taggedfeatures as taggedfeatures


@dataclass(slots=True)
class Config:
    holders: Optional[Config] = field(default_factory=Config)


@dataclass(slots=True)
class x:
    pass
