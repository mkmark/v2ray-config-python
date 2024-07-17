from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class loggerServiceClient:
    cc: Optional[ClientConnInterface] = field(default_factory=ClientConnInterface)


@dataclass(slots=True)
class loggerServiceFollowLogClient(ClientStream):
    pass


@dataclass(slots=True)
class UnimplementedLoggerServiceServer:
    pass


@dataclass(slots=True)
class loggerServiceFollowLogServer(ServerStream):
    pass
