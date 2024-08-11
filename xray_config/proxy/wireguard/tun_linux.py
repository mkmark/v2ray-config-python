from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class deviceNet(tunnel):
    dialer: Optional[Dialer] = field(default_factory=Dialer)
    handle: Optional[Handle] = field(default_factory=Handle)
    linkAddrs: Optional[list[Addr]] = field(default_factory=list[Addr])
    routes: Optional[list[Route]] = field(default_factory=list[Route])
    rules: Optional[list[Rule]] = field(default_factory=list[Rule])
