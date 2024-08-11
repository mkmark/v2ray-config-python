from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class gRPCServiceClient:
    cc: Optional[ClientConnInterface] = field(default_factory=ClientConnInterface)


@dataclass(slots=True)
class gRPCServiceTunClient(ClientStream):
    pass


@dataclass(slots=True)
class gRPCServiceTunMultiClient(ClientStream):
    pass


@dataclass(slots=True)
class UnimplementedGRPCServiceServer:
    pass


@dataclass(slots=True)
class gRPCServiceTunServer(ServerStream):
    pass


@dataclass(slots=True)
class gRPCServiceTunMultiServer(ServerStream):
    pass
