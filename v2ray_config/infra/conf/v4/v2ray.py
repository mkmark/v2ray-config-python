from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.infra.conf.cfgcommon.muxcfg.mux import MuxConfig
from v2ray_config.infra.conf.cfgcommon.proxycfg.proxy import ProxyConfig
from v2ray_config.infra.conf.cfgcommon.sniffer.sniffer import SniffingConfig
from v2ray_config.infra.conf.synthetic.dns.dns import DNSConfig
from v2ray_config.infra.conf.synthetic.dns.fakedns import FakeDNSConfig
from v2ray_config.infra.conf.synthetic.log.log import LogConfig
from v2ray_config.infra.conf.synthetic.router.router import RouterConfig
from v2ray_config.infra.conf.v4.api import APIConfig
from v2ray_config.infra.conf.v4.browser_forwarder import BrowserForwarderConfig
from v2ray_config.infra.conf.v4.observatory import (
    BurstObservatoryConfig,
    MultiObservatoryConfig,
    ObservatoryConfig,
)
from v2ray_config.infra.conf.v4.policy import PolicyConfig
from v2ray_config.infra.conf.v4.reverse import ReverseConfig
from v2ray_config.infra.conf.v4.transport import TransportConfig
from v2ray_config.infra.conf.v4.transport_internet import StreamConfig

# import v2ray_config.app.dispatcher as dispatcher
# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.app.stats as stats
# import v2ray_config.common.serial as serial
# import v2ray_config.features as features
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.infra.conf.cfgcommon.loader as loader
# import v2ray_config.infra.conf.cfgcommon.muxcfg as muxcfg
# import v2ray_config.infra.conf.cfgcommon.proxycfg as proxycfg
# import v2ray_config.infra.conf.cfgcommon.sniffer as sniffer
# import v2ray_config.infra.conf.synthetic.dns as dns
# import v2ray_config.infra.conf.synthetic.log as log
# import v2ray_config.infra.conf.synthetic.router as router


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
    stream_settings: Optional[StreamConfig] = field(default_factory=StreamConfig)
    domain_override: Optional[list[str]] = field(default_factory=list[str])
    sniffing: Optional[SniffingConfig] = field(default_factory=SniffingConfig)


@dataclass(slots=True)
class OutboundDetourConfig:
    protocol: Optional[str] = None
    send_through: Optional[str] = None
    tag: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)
    stream_settings: Optional[StreamConfig] = field(default_factory=StreamConfig)
    proxy_settings: Optional[ProxyConfig] = field(default_factory=ProxyConfig)
    mux: Optional[MuxConfig] = field(default_factory=MuxConfig)
    domain_strategy: Optional[str] = None


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
    inbound_detour: Optional[list[InboundDetourConfig]] = field(
        default_factory=list[InboundDetourConfig]
    )
    outbound_detour: Optional[list[OutboundDetourConfig]] = field(
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
    stats: Optional[StatsConfig] = field(default_factory=StatsConfig)
    reverse: Optional[ReverseConfig] = field(default_factory=ReverseConfig)
    fake_dns: Optional[FakeDNSConfig] = field(default_factory=FakeDNSConfig)
    browser_forwarder: Optional[BrowserForwarderConfig] = field(
        default_factory=BrowserForwarderConfig
    )
    observatory: Optional[ObservatoryConfig] = field(default_factory=ObservatoryConfig)
    burst_observatory: Optional[BurstObservatoryConfig] = field(
        default_factory=BurstObservatoryConfig
    )
    multi_observatory: Optional[MultiObservatoryConfig] = field(
        default_factory=MultiObservatoryConfig
    )
    services: Optional[dict[str, dict]] = field(default_factory=dict[str, dict])
