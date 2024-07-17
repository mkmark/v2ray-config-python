from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.common.protocol.server_spec_pb import ServerEndpoint

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config_DomainStrategy(int):
    pass


@dataclass(slots=True)
class DestinationOverride:
    server: Optional[ServerEndpoint] = field(default_factory=ServerEndpoint)


@dataclass(slots=True)
class Config:
    domain_strategy: Optional[Config_DomainStrategy] = field(
        default_factory=Config_DomainStrategy
    )
    timeout: Optional[int] = None
    destination_override: Optional[DestinationOverride] = field(
        default_factory=DestinationOverride
    )
    user_level: Optional[int] = None


@dataclass(slots=True)
class SimplifiedConfig:
    pass


@dataclass(slots=True)
class x:
    pass
