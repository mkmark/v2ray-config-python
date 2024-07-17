from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


# @dataclass(slots=True)
# class hMacCreator:
#     parent: Optional[hMacCreator] = field(default_factory=hMacCreator)
#     value: Optional[list[int]] = field(default_factory=list[int])
