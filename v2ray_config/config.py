from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.cmdarg as cmdarg


@dataclass(slots=True)
class ConfigFormat:
    name: Optional[list[str]] = field(default_factory=list[str])
    extension: Optional[list[str]] = field(default_factory=list[str])
    loader: Optional[ConfigLoader] = field(default_factory=ConfigLoader)
