from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf


@dataclass(slots=True)
class State(int):
    pass


@dataclass(slots=True)
class Reader(Reader):
    pending: Optional[list[int]] = field(default_factory=list[int])
    br: Optional[BufferedReader] = field(default_factory=BufferedReader)
