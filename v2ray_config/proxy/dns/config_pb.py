from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.protoext as protoext


# @dataclass(slots=True)
# class Config:
#     server: Optional[Endpoint] = field(default_factory=Endpoint)
#     user_level: Optional[int] = None


@dataclass(slots=True)
class SimplifiedConfig:
    pass


@dataclass(slots=True)
class x:
    pass
