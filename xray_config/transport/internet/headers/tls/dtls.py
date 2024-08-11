from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.dice as dice


@dataclass(slots=True)
class DTLS:
    epoch: Optional[int] = None
    length: Optional[int] = None
    sequence: Optional[int] = None
