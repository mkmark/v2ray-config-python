from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.common.protocol.server_spec_pb import ServerEndpoint

# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class Config_DomainStrategy(int):
    pass


@dataclass(slots=True)
class DestinationOverride:
    server: Optional[ServerEndpoint] = field(default_factory=ServerEndpoint)


@dataclass(slots=True)
class Fragment:
    packets_from: Optional[int] = None
    packets_to: Optional[int] = None
    length_min: Optional[int] = None
    length_max: Optional[int] = None
    interval_min: Optional[int] = None
    interval_max: Optional[int] = None


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
    fragment: Optional[Fragment] = field(default_factory=Fragment)
    proxy_protocol: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
