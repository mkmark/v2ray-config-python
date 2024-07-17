from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class routingServiceClient:
    cc: Optional[ClientConnInterface] = field(default_factory=ClientConnInterface)


@dataclass(slots=True)
class routingServiceSubscribeRoutingStatsClient(ClientStream):
    pass


@dataclass(slots=True)
class UnimplementedRoutingServiceServer:
    pass


@dataclass(slots=True)
class routingServiceSubscribeRoutingStatsServer(ServerStream):
    pass
