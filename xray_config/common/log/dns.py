from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class dnsStatus(str):
    pass


@dataclass(slots=True)
class DNSLog:
    server: Optional[str] = None
    domain: Optional[str] = None
    result: Optional[list[IP]] = field(default_factory=list[IP])
    status: Optional[dnsStatus] = field(default_factory=dnsStatus)
    elapsed: Optional[str] = None
    error: Optional[error] = field(default_factory=error)
