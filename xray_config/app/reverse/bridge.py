from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.mux as mux
# import xray_config.common.net as net
# import xray_config.common.session as session
# import xray_config.common.task as task
# import xray_config.features.routing as routing
# import xray_config.transport as transport
# import xray_config.transport.pipe as pipe


@dataclass(slots=True)
class Bridge:
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    tag: Optional[str] = None
    domain: Optional[str] = None
    workers: Optional[list[BridgeWorker]] = field(default_factory=list[BridgeWorker])
    monitorTask: Optional[Periodic] = field(default_factory=Periodic)


@dataclass(slots=True)
class BridgeWorker:
    tag: Optional[str] = None
    worker: Optional[ServerWorker] = field(default_factory=ServerWorker)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
