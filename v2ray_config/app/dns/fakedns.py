from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.dns.fakedns as fakedns
# import v2ray_config.common.net as net
# import v2ray_config.features.dns as dns


@dataclass(slots=True)
class FakeDNSClient(DNS):
    pass


@dataclass(slots=True)
class FakeDNSEngine:
    dns: Optional[DNS] = field(default_factory=DNS)
    fake_holders: Optional[HolderMulti] = field(default_factory=HolderMulti)
    fake_default: Optional[HolderMulti] = field(default_factory=HolderMulti)
