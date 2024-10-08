from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.proxy.freedom as freedom


@dataclass(slots=True)
class FreedomConfig:
    domainStrategy: Optional[str] = None
    timeout: Optional[int] = None
    redirect: Optional[str] = None
    userLevel: Optional[int] = None
