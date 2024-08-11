from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.net as net


@dataclass(slots=True)
class Conn(Conn):
    writer: Optional[VectorisedWriter] = field(default_factory=VectorisedWriter)
