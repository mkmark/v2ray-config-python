from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.proxy.freedom as freedom


@dataclass(slots=True)
class Fragment:
    packets: Optional[str] = None
    length: Optional[str] = None
    interval: Optional[str] = None


@dataclass(slots=True)
class FreedomConfig:
    domainStrategy: Optional[str] = None
    timeout: Optional[int] = None
    redirect: Optional[str] = None
    userLevel: Optional[int] = None
    fragment: Optional[Fragment] = field(default_factory=Fragment)
    proxyProtocol: Optional[int] = None
