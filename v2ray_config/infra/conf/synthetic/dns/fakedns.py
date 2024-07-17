from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.dns.fakedns as fakedns


@dataclass(slots=True)
class FakeDNSPoolElementConfig:
    ip_pool: Optional[str] = None
    pool_size: Optional[int] = None


@dataclass(slots=True)
class FakeDNSConfig:
    pool: Optional[FakeDNSPoolElementConfig] = field(default_factory=FakeDNSPoolElementConfig)
    pools: Optional[list[FakeDNSPoolElementConfig]] = field(default_factory=list[FakeDNSPoolElementConfig])


@dataclass(slots=True)
class FakeDNSConfigExtend(FakeDNSConfig):
    pass
