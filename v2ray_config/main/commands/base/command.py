from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Command:
    usageLine: Optional[str] = None
    short: Optional[str] = None
    long: Optional[str] = None
    flag: Optional[FlagSet] = field(default_factory=FlagSet)
    customFlags: Optional[bool] = None
    commands: Optional[list[Command]] = field(default_factory=list[Command])
