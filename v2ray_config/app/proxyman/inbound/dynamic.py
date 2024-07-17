from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.common.dice as dice
# import v2ray_config.common.mux as mux
# import v2ray_config.common.net as net
# import v2ray_config.common.task as task
# import v2ray_config.proxy as proxy
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class DynamicInboundHandler:
    tag: Optional[str] = None
    v: Optional[Instance] = field(default_factory=Instance)
    proxy_config: Optional[dict] = field(default_factory=dict)
    receiver_config: Optional[ReceiverConfig] = field(default_factory=ReceiverConfig)
    stream_settings: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
    port_mutex: Optional[Mutex] = field(default_factory=Mutex)
    ports_in_use: Optional[dict[int, bool]] = field(default_factory=dict[int, bool])
    worker_mutex: Optional[RWMutex] = field(default_factory=RWMutex)
    worker: Optional[list[worker]] = field(default_factory=list[worker])
    last_refresh: Optional[Time] = field(default_factory=Time)
    mux: Optional[Server] = field(default_factory=Server)
    task: Optional[Periodic] = field(default_factory=Periodic)
    ctx: Optional[Context] = field(default_factory=Context)
