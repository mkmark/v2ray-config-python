from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.mux as mux
# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.common.task as task
# import v2ray_config.features.routing as routing
# import v2ray_config.transport as transport
# import v2ray_config.transport.pipe as pipe


@dataclass(slots=True)
class Bridge:
    ctx: Optional[Context] = field(default_factory=Context)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    tag: Optional[str] = None
    domain: Optional[str] = None
    workers: Optional[list[BridgeWorker]] = field(default_factory=list[BridgeWorker])
    monitor_task: Optional[Periodic] = field(default_factory=Periodic)


@dataclass(slots=True)
class BridgeWorker:
    tag: Optional[str] = None
    worker: Optional[ServerWorker] = field(default_factory=ServerWorker)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
