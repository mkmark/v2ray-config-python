from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net
# import xray_config.features.dns as dns
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class netReadInfo:
    waiter: Optional[WaitGroup] = field(default_factory=WaitGroup)
    buff: Optional[list[int]] = field(default_factory=list[int])
    bytes: Optional[int] = None
    endpoint: Optional[Endpoint] = field(default_factory=Endpoint)
    err: Optional[error] = field(default_factory=error)


@dataclass(slots=True)
class netBind:
    dns: Optional[Client] = field(default_factory=Client)
    dnsOption: Optional[IPOption] = field(default_factory=IPOption)
    workers: Optional[int] = None
    readQueue: Optional[chan] = field(default_factory=chan)


@dataclass(slots=True)
class netBindClient(netBind):
    ctx: Optional[Context] = field(default_factory=Context)
    dialer: Optional[Dialer] = field(default_factory=Dialer)
    reserved: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class netBindServer(netBind):
    pass


@dataclass(slots=True)
class netEndpoint:
    dst: Optional[Destination] = field(default_factory=Destination)
    conn: Optional[Conn] = field(default_factory=Conn)
