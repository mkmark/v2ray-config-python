from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.proxy.wireguard.gvisortun as gvisortun


@dataclass(slots=True)
class tunCreator(Addr, mtu int, handler promiscuousModeHandler) (Tunnel, error)):
    pass


@dataclass(slots=True)
class promiscuousModeHandler(Conn)):
    pass


@dataclass(slots=True)
class tunnel:
    tun: Optional[Device] = field(default_factory=Device)
    device: Optional[Device] = field(default_factory=Device)
    rw: Optional[Mutex] = field(default_factory=Mutex)


@dataclass(slots=True)
class gvisorNet(tunnel):
    net: Optional[Net] = field(default_factory=Net)
