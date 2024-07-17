from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.dice as dice


@dataclass(slots=True)
class SRTP:
    header: Optional[int] = None
    number: Optional[int] = None
