from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.transport.internet.grpc as grpc


@dataclass(slots=True)
class GRPCConfig:
    authority: Optional[str] = None
    serviceName: Optional[str] = None
    multiMode: Optional[bool] = None
    idle_timeout: Optional[int] = None
    health_check_timeout: Optional[int] = None
    permit_without_stream: Optional[bool] = None
    initial_windows_size: Optional[int] = None
    user_agent: Optional[str] = None
