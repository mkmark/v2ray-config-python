from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.features.stats as stats


@dataclass(slots=True)
class SizeStatWriter:
    counter: Optional[Counter] = field(default_factory=Counter)
    writer: Optional[Writer] = field(default_factory=Writer)
