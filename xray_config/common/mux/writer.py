from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.serial as serial


@dataclass(slots=True)
class Writer:
    dest: Optional[Destination] = field(default_factory=Destination)
    writer: Optional[Writer] = field(default_factory=Writer)
    id: Optional[int] = None
    followup: Optional[bool] = None
    hasError: Optional[bool] = None
    transferType: Optional[TransferType] = field(default_factory=TransferType)
    globalID: Optional[[8]byte] = field(default_factory=[8]byte)
