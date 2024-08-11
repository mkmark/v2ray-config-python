from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf


@dataclass(slots=True)
class Link:
    reader: Optional[Reader] = field(default_factory=Reader)
    writer: Optional[Writer] = field(default_factory=Writer)
