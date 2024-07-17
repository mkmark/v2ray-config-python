from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class retryer:
    total_attempt: Optional[int] = None
