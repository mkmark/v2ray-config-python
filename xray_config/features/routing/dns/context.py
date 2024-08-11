from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.features.dns as dns
# import xray_config.features.routing as routing


@dataclass(slots=True)
class ResolvableContext(Context):
    dnsClient: Optional[Client] = field(default_factory=Client)
    resolvedIPs: Optional[list[IP]] = field(default_factory=list[IP])
