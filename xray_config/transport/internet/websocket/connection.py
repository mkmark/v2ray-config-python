from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.serial as serial


@dataclass(slots=True)
class connection:
    conn: Optional[Conn] = field(default_factory=Conn)
    reader: Optional[Reader] = field(default_factory=Reader)
    remoteAddr: Optional[Addr] = field(default_factory=Addr)
