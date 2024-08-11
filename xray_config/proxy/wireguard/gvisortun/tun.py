from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Net(netTun):
    pass


@dataclass(slots=True)
class netTun:
    ep: Optional[Endpoint] = field(default_factory=Endpoint)
    stack: Optional[Stack] = field(default_factory=Stack)
    events: Optional[chan] = field(default_factory=chan)
    incomingPacket: Optional[chan] = field(default_factory=chan)
    mtu: Optional[int] = None
    hasV4,: Optional[hasV6] = field(default_factory=hasV6)
