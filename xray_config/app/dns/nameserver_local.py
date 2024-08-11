from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.features.dns as dns
# import xray_config.features.dns.localdns as localdns


@dataclass(slots=True)
class LocalNameServer:
    client: Optional[Client] = field(default_factory=Client)
