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
    proxyConfig: Optional[dict] = field(default_factory=dict)
    receiverConfig: Optional[ReceiverConfig] = field(default_factory=ReceiverConfig)
    streamSettings: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
    portMutex: Optional[Mutex] = field(default_factory=Mutex)
    portsInUse: Optional[dict[int, bool]] = field(default_factory=dict[int, bool])
    workerMutex: Optional[RWMutex] = field(default_factory=RWMutex)
    worker: Optional[list[worker]] = field(default_factory=list[worker])
    lastRefresh: Optional[Time] = field(default_factory=Time)
    mux: Optional[Server] = field(default_factory=Server)
    task: Optional[Periodic] = field(default_factory=Periodic)
    ctx: Optional[Context] = field(default_factory=Context)
