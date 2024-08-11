from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.session as session
# import xray_config.common.signal.done as done
# import xray_config.common.task as task
# import xray_config.common.xudp as xudp
# import xray_config.proxy as proxy
# import xray_config.transport as transport
# import xray_config.transport.internet as internet
# import xray_config.transport.pipe as pipe


@dataclass(slots=True)
class ClientManager:
    enabled: Optional[bool] = None
    picker: Optional[WorkerPicker] = field(default_factory=WorkerPicker)


@dataclass(slots=True)
class IncrementalWorkerPicker:
    factory: Optional[ClientWorkerFactory] = field(default_factory=ClientWorkerFactory)
    access: Optional[Mutex] = field(default_factory=Mutex)
    workers: Optional[list[ClientWorker]] = field(default_factory=list[ClientWorker])
    cleanupTask: Optional[Periodic] = field(default_factory=Periodic)


@dataclass(slots=True)
class DialingWorkerFactory:
    proxy: Optional[Outbound] = field(default_factory=Outbound)
    dialer: Optional[Dialer] = field(default_factory=Dialer)
    strategy: Optional[ClientStrategy] = field(default_factory=ClientStrategy)


@dataclass(slots=True)
class ClientStrategy:
    maxConcurrency: Optional[int] = None
    maxConnection: Optional[int] = None


@dataclass(slots=True)
class ClientWorker:
    sessionManager: Optional[SessionManager] = field(default_factory=SessionManager)
    link: Optional[Link] = field(default_factory=Link)
    done: Optional[Instance] = field(default_factory=Instance)
    strategy: Optional[ClientStrategy] = field(default_factory=ClientStrategy)
