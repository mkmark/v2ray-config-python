from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.proxy.dokodemo as dokodemo


@dataclass(slots=True)
class DokodemoConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    network: Optional[list[str]] = field(default_factory=list[str])
    timeout: Optional[int] = None
    followRedirect: Optional[bool] = None
    userLevel: Optional[int] = None
