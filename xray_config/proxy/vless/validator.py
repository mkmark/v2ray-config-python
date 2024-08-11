from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol
# import xray_config.common.uuid as uuid


@dataclass(slots=True)
class Validator:
    email: Optional[Map] = field(default_factory=Map)
    users: Optional[Map] = field(default_factory=Map)
