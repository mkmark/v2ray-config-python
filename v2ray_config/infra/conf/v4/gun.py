from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet.grpc as grpc


@dataclass(slots=True)
class GunConfig:
    serviceName: Optional[str] = None
