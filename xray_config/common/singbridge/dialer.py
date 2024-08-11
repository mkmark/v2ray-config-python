from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net
# import xray_config.common.net.cnc as cnc
# import xray_config.common.session as session
# import xray_config.proxy as proxy
# import xray_config.transport as transport
# import xray_config.transport.internet as internet
# import xray_config.transport.pipe as pipe


@dataclass(slots=True)
class XrayDialer(Dialer):
    pass


@dataclass(slots=True)
class XrayOutboundDialer:
    outbound: Optional[Outbound] = field(default_factory=Outbound)
    dialer: Optional[Dialer] = field(default_factory=Dialer)
