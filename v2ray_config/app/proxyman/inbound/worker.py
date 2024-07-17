from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.environment as environment
# import v2ray_config.common.environment.envctx as envctx
# import v2ray_config.common.net as net
# import v2ray_config.common.serial as serial
# import v2ray_config.common.session as session
# import v2ray_config.common.signal.done as done
# import v2ray_config.common.task as task
# import v2ray_config.features.routing as routing
# import v2ray_config.features.stats as stats
# import v2ray_config.proxy as proxy
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tcp as tcp
# import v2ray_config.transport.internet.udp as udp
# import v2ray_config.transport.pipe as pipe


@dataclass(slots=True)
class tcpWorker:
    address: Optional[str] = None
    port: Optional[int] = None
    proxy: Optional[Inbound] = field(default_factory=Inbound)
    stream: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
    recv_orig_dest: Optional[bool] = None
    tag: Optional[str] = None
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    sniffing_config: Optional[SniffingConfig] = field(default_factory=SniffingConfig)
    uplink_counter: Optional[Counter] = field(default_factory=Counter)
    downlink_counter: Optional[Counter] = field(default_factory=Counter)
    hub: Optional[Listener] = field(default_factory=Listener)
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class udpConn:
    last_activity_time: Optional[int] = None
    reader: Optional[Reader] = field(default_factory=Reader)
    writer: Optional[Writer] = field(default_factory=Writer)
    remote: Optional[Addr] = field(default_factory=Addr)
    local: Optional[Addr] = field(default_factory=Addr)
    done: Optional[Instance] = field(default_factory=Instance)
    uplink: Optional[Counter] = field(default_factory=Counter)
    downlink: Optional[Counter] = field(default_factory=Counter)
    inactive: Optional[bool] = None


@dataclass(slots=True)
class connID:
    src: Optional[Destination] = field(default_factory=Destination)
    dest: Optional[Destination] = field(default_factory=Destination)


@dataclass(slots=True)
class udpWorker(RWMutex):
    proxy: Optional[Inbound] = field(default_factory=Inbound)
    hub: Optional[Hub] = field(default_factory=Hub)
    address: Optional[str] = None
    port: Optional[int] = None
    tag: Optional[str] = None
    stream: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    sniffing_config: Optional[SniffingConfig] = field(default_factory=SniffingConfig)
    uplink_counter: Optional[Counter] = field(default_factory=Counter)
    downlink_counter: Optional[Counter] = field(default_factory=Counter)
    checker: Optional[Periodic] = field(default_factory=Periodic)
    active_conn: Optional[dict[connID, udpConn]] = field(default_factory=dict[connID, udpConn])
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class dsWorker:
    address: Optional[str] = None
    proxy: Optional[Inbound] = field(default_factory=Inbound)
    stream: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
    tag: Optional[str] = None
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    sniffing_config: Optional[SniffingConfig] = field(default_factory=SniffingConfig)
    uplink_counter: Optional[Counter] = field(default_factory=Counter)
    downlink_counter: Optional[Counter] = field(default_factory=Counter)
    hub: Optional[Listener] = field(default_factory=Listener)
    ctx: Optional[Context] = field(default_factory=Context)
