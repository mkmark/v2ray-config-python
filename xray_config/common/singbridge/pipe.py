from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.transport as transport


@dataclass(slots=True)
class PipeConnWrapper(Conn):
    r: Optional[Reader] = field(default_factory=Reader)
    w: Optional[Writer] = field(default_factory=Writer)
