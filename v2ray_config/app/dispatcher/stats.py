from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.features.stats as stats


@dataclass(slots=True)
class SizeStatWriter:
    counter: Optional[Counter] = field(default_factory=Counter)
    writer: Optional[Writer] = field(default_factory=Writer)
