from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.serial as serial
# import xray_config.proxy.blackhole as blackhole


@dataclass(slots=True)
class NoneResponse:
    pass


@dataclass(slots=True)
class HTTPResponse:
    pass


@dataclass(slots=True)
class BlackholeConfig:
    response: Optional[dict] = field(default_factory=dict)
