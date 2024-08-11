from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.bitmask as bitmask
# import xray_config.common.net as net
# import xray_config.common.uuid as uuid


@dataclass(slots=True)
class RequestCommand(int):
    pass


@dataclass(slots=True)
class RequestHeader:
    version: Optional[int] = None
    command: Optional[RequestCommand] = field(default_factory=RequestCommand)
    option: Optional[Byte] = field(default_factory=Byte)
    security: Optional[SecurityType] = field(default_factory=SecurityType)
    port: Optional[int] = None
    address: Optional[str] = None
    user: Optional[MemoryUser] = field(default_factory=MemoryUser)


@dataclass(slots=True)
class ResponseHeader:
    option: Optional[Byte] = field(default_factory=Byte)
    command: Optional[ResponseCommand] = field(default_factory=ResponseCommand)


@dataclass(slots=True)
class CommandSwitchAccount:
    host: Optional[str] = None
    port: Optional[int] = None
    iD: Optional[UUID] = field(default_factory=UUID)
    level: Optional[int] = None
    validMin: Optional[int] = None
