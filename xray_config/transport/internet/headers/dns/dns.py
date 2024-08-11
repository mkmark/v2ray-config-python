from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.dice as dice


@dataclass(slots=True)
class DNS:
    header: Optional[list[int]] = field(default_factory=list[int])
