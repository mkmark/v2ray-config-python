from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class Writer:
    dest: Optional[Destination] = field(default_factory=Destination)
    writer: Optional[Writer] = field(default_factory=Writer)
    id: Optional[int] = None
    followup: Optional[bool] = None
    has_error: Optional[bool] = None
    transfer_type: Optional[TransferType] = field(default_factory=TransferType)
