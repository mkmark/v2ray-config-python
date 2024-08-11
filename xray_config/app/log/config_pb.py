from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# from xray_config.common.log.log_pb import Severity

# import xray_config.common.log as log


@dataclass(slots=True)
class LogType(int):
    pass


@dataclass(slots=True)
class Config:
    error_log_type: Optional[LogType] = field(default_factory=LogType)
    error_log_level: Optional[str] = None
    error_log_path: Optional[str] = None
    access_log_type: Optional[LogType] = field(default_factory=LogType)
    access_log_path: Optional[str] = None
    enable_dns_log: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
