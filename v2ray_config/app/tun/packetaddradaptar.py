from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.tun.device as device
# import v2ray_config.app.tun.tunsorter as tunsorter


@dataclass(slots=True)
class packetAddrDevice(Device):
    sorter: Optional[TunSorter] = field(default_factory=TunSorter)
    secondaryDispatcher: Optional[NetworkDispatcher] = field(default_factory=NetworkDispatcher)
