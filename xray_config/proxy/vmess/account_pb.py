from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class Account:
    id: Optional[str] = None
    security_settings: Optional[SecurityConfig] = field(default_factory=SecurityConfig)
    tests_enabled: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
