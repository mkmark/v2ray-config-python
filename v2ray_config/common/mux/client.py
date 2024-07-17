from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.session as session
# import v2ray_config.common.signal.done as done
# import v2ray_config.common.task as task
# import v2ray_config.proxy as proxy
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.pipe as pipe


@dataclass(slots=True)
class ClientManager:
    enabled: Optional[bool] = None
    picker: Optional[WorkerPicker] = field(default_factory=WorkerPicker)


@dataclass(slots=True)
class IncrementalWorkerPicker:
    factory: Optional[ClientWorkerFactory] = field(default_factory=ClientWorkerFactory)
    access: Optional[Mutex] = field(default_factory=Mutex)
    workers: Optional[list[ClientWorker]] = field(default_factory=list[ClientWorker])
    cleanup_task: Optional[Periodic] = field(default_factory=Periodic)


@dataclass(slots=True)
class DialingWorkerFactory:
    proxy: Optional[Outbound] = field(default_factory=Outbound)
    dialer: Optional[Dialer] = field(default_factory=Dialer)
    strategy: Optional[ClientStrategy] = field(default_factory=ClientStrategy)
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class ClientStrategy:
    max_concurrency: Optional[int] = None
    max_connection: Optional[int] = None


@dataclass(slots=True)
class ClientWorker:
    session_manager: Optional[SessionManager] = field(default_factory=SessionManager)
    link: Optional[Link] = field(default_factory=Link)
    done: Optional[Instance] = field(default_factory=Instance)
    strategy: Optional[ClientStrategy] = field(default_factory=ClientStrategy)
