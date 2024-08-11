from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors


@dataclass(slots=True)
class BufferedReader:
    reader: Optional[Reader] = field(default_factory=Reader)
    buffer: Optional[MultiBuffer] = field(default_factory=MultiBuffer)


@dataclass(slots=True)
class SingleReader(Reader):
    pass


@dataclass(slots=True)
class PacketReader(Reader):
    pass
