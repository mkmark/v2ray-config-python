from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class FakeDnsPool:
    ip_pool: Optional[str] = None
    lruSize: Optional[int] = None


@dataclass(slots=True)
class FakeDnsPoolMulti:
    pools: Optional[list[FakeDnsPool]] = field(default_factory=list[FakeDnsPool])


@dataclass(slots=True)
class x:
    pass
