from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.uuid as uuid


@dataclass(slots=True)
class Validator:
    email: Optional[Map] = field(default_factory=Map)
    users: Optional[Map] = field(default_factory=Map)
