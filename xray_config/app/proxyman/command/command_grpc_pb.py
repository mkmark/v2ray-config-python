from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class handlerServiceClient:
    cc: Optional[ClientConnInterface] = field(default_factory=ClientConnInterface)


@dataclass(slots=True)
class UnimplementedHandlerServiceServer:
    pass
