from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.uuid as uuid


@dataclass(slots=True)
class ID:
    uuid: Optional[UUID] = field(default_factory=UUID)
    cmdKey: Optional[[IDBytesLen]byte] = field(default_factory=[IDBytesLen]byte)
