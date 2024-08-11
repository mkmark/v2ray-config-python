from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.infra.conf.api import APIConfig
from xray_config.infra.conf.dns import DNSConfig
from xray_config.infra.conf.fakedns import FakeDNSConfig
from xray_config.infra.conf.log import LogConfig
from xray_config.infra.conf.metrics import MetricsConfig
from xray_config.infra.conf.observatory import BurstObservatoryConfig, ObservatoryConfig
from xray_config.infra.conf.policy import PolicyConfig
from xray_config.infra.conf.reverse import ReverseConfig
from xray_config.infra.conf.router import RouterConfig
from xray_config.infra.conf.transport import TransportConfig
from xray_config.infra.conf.transport_internet import ProxyConfig, StreamConfig

# import xray_config.app.dispatcher as dispatcher
# import xray_config.app.proxyman as proxyman
# import xray_config.app.stats as stats
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.serial as serial
# import xray_config.core as core
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class SniffingConfig:
    enabled: Optional[bool] = None
    destOverride: Optional[list[str]] = field(default_factory=list[str])
    domainsExcluded: Optional[list[str]] = field(default_factory=list[str])
    metadataOnly: Optional[bool] = None
    routeOnly: Optional[bool] = None


@dataclass(slots=True)
class MuxConfig:
    enabled: Optional[bool] = None
    concurrency: Optional[int] = None
    xudpConcurrency: Optional[int] = None
    xudpProxyUDP443: Optional[str] = None


@dataclass(slots=True)
class InboundDetourAllocationConfig:
    strategy: Optional[str] = None
    concurrency: Optional[int] = None
    refresh: Optional[int] = None


@dataclass(slots=True)
class InboundDetourConfig:
    protocol: Optional[str] = None
    port: Optional[int] = None
    listen: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)
    tag: Optional[str] = None
    allocate: Optional[InboundDetourAllocationConfig] = field(
        default_factory=InboundDetourAllocationConfig
    )
    streamSettings: Optional[StreamConfig] = field(default_factory=StreamConfig)
    domainOverride: Optional[list[str]] = field(default_factory=list[str])
    sniffing: Optional[SniffingConfig] = field(default_factory=SniffingConfig)


@dataclass(slots=True)
class OutboundDetourConfig:
    protocol: Optional[str] = None
    sendThrough: Optional[str] = None
    tag: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)
    streamSettings: Optional[StreamConfig] = field(default_factory=StreamConfig)
    proxySettings: Optional[ProxyConfig] = field(default_factory=ProxyConfig)
    mux: Optional[MuxConfig] = field(default_factory=MuxConfig)


@dataclass(slots=True)
class StatsConfig:
    pass


@dataclass(slots=True)
class Config:
    port: Optional[int] = None
    inbound: Optional[InboundDetourConfig] = field(default_factory=InboundDetourConfig)
    outbound: Optional[OutboundDetourConfig] = field(
        default_factory=OutboundDetourConfig
    )
    inboundDetour: Optional[list[InboundDetourConfig]] = field(
        default_factory=list[InboundDetourConfig]
    )
    outboundDetour: Optional[list[OutboundDetourConfig]] = field(
        default_factory=list[OutboundDetourConfig]
    )
    log: Optional[LogConfig] = field(default_factory=LogConfig)
    routing: Optional[RouterConfig] = field(default_factory=RouterConfig)
    dns: Optional[DNSConfig] = field(default_factory=DNSConfig)
    inbounds: Optional[list[InboundDetourConfig]] = field(
        default_factory=list[InboundDetourConfig]
    )
    outbounds: Optional[list[OutboundDetourConfig]] = field(
        default_factory=list[OutboundDetourConfig]
    )
    transport: Optional[TransportConfig] = field(default_factory=TransportConfig)
    policy: Optional[PolicyConfig] = field(default_factory=PolicyConfig)
    api: Optional[APIConfig] = field(default_factory=APIConfig)
    metrics: Optional[MetricsConfig] = field(default_factory=MetricsConfig)
    stats: Optional[StatsConfig] = field(default_factory=StatsConfig)
    reverse: Optional[ReverseConfig] = field(default_factory=ReverseConfig)
    fakeDns: Optional[FakeDNSConfig] = field(default_factory=FakeDNSConfig)
    observatory: Optional[ObservatoryConfig] = field(default_factory=ObservatoryConfig)
    burstObservatory: Optional[BurstObservatoryConfig] = field(
        default_factory=BurstObservatoryConfig
    )
