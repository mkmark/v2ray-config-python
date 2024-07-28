from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.mux as mux
# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.common.task as task
# import v2ray_config.features.outbound as outbound
# import v2ray_config.transport as transport
# import v2ray_config.transport.pipe as pipe


@dataclass(slots=True)
class Portal:
    ctx: Optional[Context] = field(default_factory=Context)
    ohm: Optional[Manager] = field(default_factory=Manager)
    tag: Optional[str] = None
    domain: Optional[str] = None
    picker: Optional[StaticMuxPicker] = field(default_factory=StaticMuxPicker)
    client: Optional[ClientManager] = field(default_factory=ClientManager)


@dataclass(slots=True)
class Outbound:
    portal: Optional[Portal] = field(default_factory=Portal)
    tag: Optional[str] = None


@dataclass(slots=True)
class StaticMuxPicker:
    access: Optional[Mutex] = field(default_factory=Mutex)
    workers: Optional[list[PortalWorker]] = field(default_factory=list[PortalWorker])
    cTask: Optional[Periodic] = field(default_factory=Periodic)


@dataclass(slots=True)
class PortalWorker:
    client: Optional[ClientWorker] = field(default_factory=ClientWorker)
    control: Optional[Periodic] = field(default_factory=Periodic)
    writer: Optional[Writer] = field(default_factory=Writer)
    reader: Optional[Reader] = field(default_factory=Reader)
    draining: Optional[bool] = None
