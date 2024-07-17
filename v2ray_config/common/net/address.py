from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class AddressFamily(int):
    pass


@dataclass(slots=True)
class ipv4Address(list[int]):
    pass


@dataclass(slots=True)
class ipv6Address(list[int]):
    pass


@dataclass(slots=True)
class domainAddress(str):
    pass
