from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net


@dataclass(slots=True)
class version(int):
    pass


@dataclass(slots=True)
class SniffHeader:
    host: Optional[str] = None
