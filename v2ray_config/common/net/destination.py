from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Destination:
    address: Optional[str] = None
    port: Optional[int] = None
    network: Optional[str] = None
