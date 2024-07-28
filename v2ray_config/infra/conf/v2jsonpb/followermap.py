from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class V2JsonProtobufMapFollower(Map):
    valueKind: Optional[FieldDescriptor] = field(default_factory=FieldDescriptor)
