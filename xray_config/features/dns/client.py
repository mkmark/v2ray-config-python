from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.serial as serial
# import xray_config.features as features


@dataclass(slots=True)
class RCodeError(int):
    pass


@dataclass(slots=True)
class IPOption:
    iPv4Enable: Optional[bool] = None
    iPv6Enable: Optional[bool] = None
    fakeEnable: Optional[bool] = None
