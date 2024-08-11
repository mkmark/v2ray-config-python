from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.dns.fakedns as fakedns
# import xray_config.common.errors as errors
# import xray_config.features.dns as dns


@dataclass(slots=True)
class FakeDNSPoolElementConfig:
    ipPool: Optional[str] = None
    poolSize: Optional[int] = None


@dataclass(slots=True)
class FakeDNSConfig:
    pool: Optional[FakeDNSPoolElementConfig] = field(default_factory=FakeDNSPoolElementConfig)
    pools: Optional[list[FakeDNSPoolElementConfig]] = field(default_factory=list[FakeDNSPoolElementConfig])


@dataclass(slots=True)
class FakeDNSPostProcessingStage:
    pass
