from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net
# import xray_config.common.serial as serial
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class KnownProtocols(int):
    pass


@dataclass(slots=True)
class AllocationStrategy_Type(int):
    pass


@dataclass(slots=True)
class InboundConfig:
    pass


@dataclass(slots=True)
class AllocationStrategy:
    type: Optional[AllocationStrategy_Type] = field(
        default_factory=AllocationStrategy_Type
    )
    concurrency: Optional[AllocationStrategy_AllocationStrategyConcurrency] = field(
        default_factory=AllocationStrategy_AllocationStrategyConcurrency
    )
    refresh: Optional[AllocationStrategy_AllocationStrategyRefresh] = field(
        default_factory=AllocationStrategy_AllocationStrategyRefresh
    )


@dataclass(slots=True)
class SniffingConfig:
    enabled: Optional[bool] = None
    destination_override: Optional[list[str]] = field(default_factory=list[str])
    domains_excluded: Optional[list[str]] = field(default_factory=list[str])
    metadata_only: Optional[bool] = None
    route_only: Optional[bool] = None


@dataclass(slots=True)
class ReceiverConfig:
    port_list: Optional[list[str]] = field(default_factory=list[str])
    listen: Optional[str] = None
    allocation_strategy: Optional[AllocationStrategy] = field(
        default_factory=AllocationStrategy
    )
    stream_settings: Optional[StreamConfig] = field(default_factory=StreamConfig)
    receive_original_destination: Optional[bool] = None
    domain_override: Optional[list[KnownProtocols]] = field(
        default_factory=list[KnownProtocols]
    )
    sniffing_settings: Optional[SniffingConfig] = field(default_factory=SniffingConfig)


@dataclass(slots=True)
class InboundHandlerConfig:
    tag: Optional[str] = None
    receiver_settings: Optional[dict] = field(default_factory=dict)
    proxy_settings: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class OutboundConfig:
    pass


@dataclass(slots=True)
class SenderConfig:
    via: Optional[str] = None
    stream_settings: Optional[StreamConfig] = field(default_factory=StreamConfig)
    proxy_settings: Optional[ProxyConfig] = field(default_factory=ProxyConfig)
    multiplex_settings: Optional[MultiplexingConfig] = field(
        default_factory=MultiplexingConfig
    )
    via_cidr: Optional[str] = None


@dataclass(slots=True)
class MultiplexingConfig:
    enabled: Optional[bool] = None
    concurrency: Optional[int] = None
    xudpConcurrency: Optional[int] = None
    xudpProxyUDP443: Optional[str] = None


@dataclass(slots=True)
class AllocationStrategy_AllocationStrategyConcurrency:
    value: Optional[int] = None


@dataclass(slots=True)
class AllocationStrategy_AllocationStrategyRefresh:
    value: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
