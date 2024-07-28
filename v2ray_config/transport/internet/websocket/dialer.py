from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.features.extension as extension
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.security as security


@dataclass(slots=True)
class dialerWithEarlyData:
    dialer: Optional[Dialer] = field(default_factory=Dialer)
    uriBase: Optional[str] = None
    config: Optional[Config] = field(default_factory=Config)


@dataclass(slots=True)
class dialerWithEarlyDataRelayed:
    forwarder: Optional[BrowserForwarder] = field(default_factory=BrowserForwarder)
    uriBase: Optional[str] = None
    config: Optional[Config] = field(default_factory=Config)
