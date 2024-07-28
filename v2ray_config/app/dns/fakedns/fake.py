from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.cache as cache
# import v2ray_config.common.net as net
# import v2ray_config.features.dns as dns


@dataclass(slots=True)
class Holder:
    domainToIP: Optional[Lru] = field(default_factory=Lru)
    nextIP: Optional[Int] = field(default_factory=Int)
    mu: Optional[Mutex] = field(default_factory=Mutex)
    ipRange: Optional[IPNet] = field(default_factory=IPNet)
    config: Optional[FakeDnsPool] = field(default_factory=FakeDnsPool)


@dataclass(slots=True)
class HolderMulti:
    holders: Optional[list[Holder]] = field(default_factory=list[Holder])
