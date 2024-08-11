from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.crypto as crypto
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.serial as serial


@dataclass(slots=True)
class PacketReader:
    reader: Optional[Reader] = field(default_factory=Reader)
    eof: Optional[bool] = None
    dest: Optional[Destination] = field(default_factory=Destination)
