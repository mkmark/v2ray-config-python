from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.net as net


@dataclass(slots=True)
class Version(int):
    pass


@dataclass(slots=True)
class SniffHeader:
    version: Optional[Version] = field(default_factory=Version)
    host: Optional[str] = None
