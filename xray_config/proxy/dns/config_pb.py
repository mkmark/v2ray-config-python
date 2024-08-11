from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.common.net.destination_pb import Endpoint

# import xray_config.common.net as net


@dataclass(slots=True)
class Config:
    server: Optional[Endpoint] = field(default_factory=Endpoint)
    user_level: Optional[int] = None
    non_IP_query: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
