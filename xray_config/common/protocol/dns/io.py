from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.serial as serial


@dataclass(slots=True)
class UDPReader(Reader):
    access: Optional[Mutex] = field(default_factory=Mutex)
    cache: Optional[MultiBuffer] = field(default_factory=MultiBuffer)


@dataclass(slots=True)
class TCPReader:
    reader: Optional[BufferedReader] = field(default_factory=BufferedReader)


@dataclass(slots=True)
class UDPWriter(Writer):
    pass


@dataclass(slots=True)
class TCPWriter(Writer):
    pass
