from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.proxy.dns as dns


@dataclass(slots=True)
class DNSOutboundConfig:
    network: Optional[str] = None
    address: Optional[str] = None
    port: Optional[int] = None
    userLevel: Optional[int] = None
    nonIPQuery: Optional[str] = None
