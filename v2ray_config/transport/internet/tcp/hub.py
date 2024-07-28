from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.serial as serial
# import v2ray_config.common.session as session
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Listener:
    listener: Optional[Listener] = field(default_factory=Listener)
    tlsConfig: Optional[Config] = field(default_factory=Config)
    authConfig: Optional[ConnectionAuthenticator] = field(default_factory=ConnectionAuthenticator)
    config: Optional[Config] = field(default_factory=Config)
    addConn: Optional[ConnHandler] = field(default_factory=ConnHandler)
