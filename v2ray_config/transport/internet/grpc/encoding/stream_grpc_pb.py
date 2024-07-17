from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class gunServiceClient:
    cc: Optional[ClientConnInterface] = field(default_factory=ClientConnInterface)


@dataclass(slots=True)
class gunServiceTunClient(ClientStream):
    pass


@dataclass(slots=True)
class UnimplementedGunServiceServer:
    pass


@dataclass(slots=True)
class gunServiceTunServer(ServerStream):
    pass
