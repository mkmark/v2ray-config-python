from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class V2JsonProtobufAnyTypeDescriptor(MessageDescriptor):
    pass


@dataclass(slots=True)
class V2JsonProtobufAnyTypeFields(FieldDescriptors):
    pass


@dataclass(slots=True)
class V2JsonProtobufAnyTypeFieldDescriptor(FieldDescriptor):
    pass


@dataclass(slots=True)
class V2JsonProtobufAnyValueField(FieldDescriptor):
    name: Optional[str] = None


@dataclass(slots=True)
class V2JsonProtobufAnyValueFieldReturn(Message):
    pass
