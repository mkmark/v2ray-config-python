from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.environment.envctx as envctx
# import v2ray_config.common.environment.filesystemcap as filesystemcap
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class fileRead:
    filename: Optional[str] = None
    field: Optional[str] = None


@dataclass(slots=True)
class pendingWrite:
    field: Optional[FieldDescriptor] = field(default_factory=FieldDescriptor)
    value: Optional[Value] = field(default_factory=Value)
