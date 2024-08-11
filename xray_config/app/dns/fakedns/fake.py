from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.cache as cache
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.features.dns as dns


@dataclass(slots=True)
class Holder:
    domainToIP: Optional[Lru] = field(default_factory=Lru)
    ipRange: Optional[IPNet] = field(default_factory=IPNet)
    mu: Optional[Mutex] = field(default_factory=Mutex)
    config: Optional[FakeDnsPool] = field(default_factory=FakeDnsPool)


@dataclass(slots=True)
class HolderMulti:
    holders: Optional[list[Holder]] = field(default_factory=list[Holder])
    config: Optional[FakeDnsPoolMulti] = field(default_factory=FakeDnsPoolMulti)
