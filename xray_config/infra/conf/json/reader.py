from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf


@dataclass(slots=True)
class State(int):
    pass


@dataclass(slots=True)
class Reader(Reader):
    br: Optional[BufferedReader] = field(default_factory=BufferedReader)
