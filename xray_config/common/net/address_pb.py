from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class IPOrDomain:
    address: Optional[isIPOrDomain_Address] = field(default_factory=isIPOrDomain_Address)


@dataclass(slots=True)
class IPOrDomain_Ip:
    ip: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class IPOrDomain_Domain:
    domain: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
