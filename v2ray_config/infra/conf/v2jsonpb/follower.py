from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class V2JsonProtobufFollowerFieldDescriptor(FieldDescriptor):
    pass


@dataclass(slots=True)
class V2JsonProtobufFollower(Message):
    pass


@dataclass(slots=True)
class V2JsonProtobufFollowerDescriptor(MessageDescriptor):
    pass


@dataclass(slots=True)
class V2JsonProtobufFollowerFields(FieldDescriptors):
    pass
