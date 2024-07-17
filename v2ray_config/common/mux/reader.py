from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.crypto as crypto
# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class PacketReader:
    reader: Optional[Reader] = field(default_factory=Reader)
    eof: Optional[bool] = None
