from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.net as net
# import xray_config.common.signal.done as done


@dataclass(slots=True)
class ConnectionOption(func(*connection)):
    pass


@dataclass(slots=True)
class connection:
    reader: Optional[BufferedReader] = field(default_factory=BufferedReader)
    writer: Optional[Writer] = field(default_factory=Writer)
    done: Optional[Instance] = field(default_factory=Instance)
    onClose: Optional[Closer] = field(default_factory=Closer)
    local: Optional[Addr] = field(default_factory=Addr)
    remote: Optional[Addr] = field(default_factory=Addr)
