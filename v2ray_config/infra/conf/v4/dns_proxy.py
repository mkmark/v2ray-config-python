from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.proxy.dns as dns


@dataclass(slots=True)
class DNSOutboundConfig:
    network: Optional[str] = None
    address: Optional[str] = None
    port: Optional[int] = None
    userLevel: Optional[int] = None
