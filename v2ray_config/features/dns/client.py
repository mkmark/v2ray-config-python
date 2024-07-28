from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.common.serial as serial
# import v2ray_config.features as features


@dataclass(slots=True)
class RCodeError(int):
    pass


@dataclass(slots=True)
class IPOption:
    iPv4Enable: Optional[bool] = None
    iPv6Enable: Optional[bool] = None
    fakeEnable: Optional[bool] = None
