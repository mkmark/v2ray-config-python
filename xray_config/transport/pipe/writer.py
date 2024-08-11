from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf


@dataclass(slots=True)
class Writer:
    pipe: Optional[pipe] = field(default_factory=pipe)
