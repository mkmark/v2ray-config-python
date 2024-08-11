from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net


@dataclass(slots=True)
class EndpointOverrideReader(Reader):
    dest: Optional[str] = None
    originalDest: Optional[str] = None


@dataclass(slots=True)
class EndpointOverrideWriter(Writer):
    dest: Optional[str] = None
    originalDest: Optional[str] = None
