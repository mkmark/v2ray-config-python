from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class statsServiceClient:
    cc: Optional[ClientConnInterface] = field(default_factory=ClientConnInterface)


@dataclass(slots=True)
class UnimplementedStatsServiceServer:
    pass
