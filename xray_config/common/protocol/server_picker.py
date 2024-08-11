from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class ServerList(RWMutex):
    servers: Optional[list[ServerSpec]] = field(default_factory=list[ServerSpec])


@dataclass(slots=True)
class RoundRobinServerPicker(Mutex):
    serverlist: Optional[ServerList] = field(default_factory=ServerList)
    nextIndex: Optional[int] = None
