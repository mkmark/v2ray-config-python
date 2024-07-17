from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.serial as serial
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.infra.conf.cfgcommon.loader as loader
# import v2ray_config.proxy.blackhole as blackhole


@dataclass(slots=True)
class NoneResponse:
    pass


@dataclass(slots=True)
class HTTPResponse:
    pass


@dataclass(slots=True)
class BlackholeConfig:
    response: Optional[dict] = field(default_factory=dict)
