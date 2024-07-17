from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.features.dns as dns


@dataclass(slots=True)
class FakeDNSServer:
    fake_dns_engine: Optional[FakeDNSEngine] = field(default_factory=FakeDNSEngine)
