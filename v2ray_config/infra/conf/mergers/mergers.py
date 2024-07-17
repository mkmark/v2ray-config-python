from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.infra.conf.json as json


@dataclass(slots=True)
class Merger:
    name: Optional[str] = None
    extensions: Optional[list[str]] = field(default_factory=list[str])
    merge: Optional[MergeFunc] = field(default_factory=MergeFunc)
