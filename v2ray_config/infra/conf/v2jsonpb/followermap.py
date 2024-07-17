from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class V2JsonProtobufMapFollower(Map):
    value_kind: Optional[FieldDescriptor] = field(default_factory=FieldDescriptor)
