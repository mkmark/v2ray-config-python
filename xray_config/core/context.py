from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class XrayKey(int):
    pass
