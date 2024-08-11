from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.platform as platform


@dataclass(slots=True)
class EnvFlag:
    name: Optional[str] = None
    altName: Optional[str] = None
