from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

import v2ray_config.app.dns
from v2ray_config.infra.conf.cfgcommon.muxcfg.mux import MuxConfig
from v2ray_config.infra.conf.cfgcommon.proxycfg.proxy import ProxyConfig
from v2ray_config.infra.conf.cfgcommon.sniffer.sniffer import SniffingConfig
from v2ray_config.infra.conf.cfgcommon.socketcfg.socket import SocketConfig
from v2ray_config.infra.conf.synthetic.dns.dns import DNSConfig
from v2ray_config.infra.conf.synthetic.log.log import LogConfig
import v2ray_config.app.router.config_pb

# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.infra.conf.cfgcommon.muxcfg as muxcfg
# import v2ray_config.infra.conf.cfgcommon.proxycfg as proxycfg
# import v2ray_config.infra.conf.cfgcommon.sniffer as sniffer
# import v2ray_config.infra.conf.cfgcommon.socketcfg as socketcfg


@dataclass(slots=True)
class StreamConfig:
    transport: Optional[str] = None
    transportSettings: Optional[dict] = field(default_factory=dict)
    security: Optional[str] = None
    securitySettings: Optional[dict] = field(default_factory=dict)
    socketSettings: Optional[SocketConfig] = field(default_factory=SocketConfig)


@dataclass(slots=True)
class InboundConfig:
    protocol: Optional[str] = None
    port: Optional[int | str] = None
    listen: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)
    tag: Optional[str] = None
    sniffing: Optional[SniffingConfig] = field(default_factory=SniffingConfig)
    streamSettings: Optional[StreamConfig] = field(default_factory=StreamConfig)


@dataclass(slots=True)
class OutboundConfig:
    protocol: Optional[str] = None
    sendThrough: Optional[str] = None
    tag: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)
    streamSettings: Optional[StreamConfig] = field(default_factory=StreamConfig)
    proxySettings: Optional[ProxyConfig] = field(default_factory=ProxyConfig)
    mux: Optional[MuxConfig] = field(default_factory=MuxConfig)
    domainStrategy: Optional[str] = None


@dataclass(slots=True)
class RootConfig:
    log: Optional[v2ray_config.app.log.config_pb.Config] = field(
        default_factory=v2ray_config.app.log.config_pb.Config
    )
    dns: Optional[v2ray_config.app.dns.config_pb.Config] = field(
        default_factory=v2ray_config.app.dns.config_pb.Config
    )
    router: Optional[v2ray_config.app.router.config_pb.Config] = field(
        default_factory=v2ray_config.app.router.config_pb.Config
    )
    inbounds: Optional[list[InboundConfig]] = field(default_factory=list[InboundConfig])
    outbounds: Optional[list[OutboundConfig]] = field(
        default_factory=list[OutboundConfig]
    )
    services: Optional[dict[str, dict]] = field(default_factory=dict[str, dict])
    extension: Optional[list[dict]] = field(default_factory=list[dict])
