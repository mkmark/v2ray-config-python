from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.serial as serial
# import v2ray_config.infra.conf.v5cfg as v5cfg


@dataclass(slots=True)
class namedStub(list[ItemStub]):
    pass


@dataclass(slots=True)
class ItemStub:
    type: Optional[str] = None
    tag: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)
