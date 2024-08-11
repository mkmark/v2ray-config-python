from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.core as core
# import xray_config.features.dns as dns


@dataclass(slots=True)
class FakeDNSServer:
    fakeDNSEngine: Optional[FakeDNSEngine] = field(default_factory=FakeDNSEngine)
