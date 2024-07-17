from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.errors as errors
# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class MultiBuffer(list[Buffer]):
    pass


@dataclass(slots=True)
class MultiBufferContainer(MultiBuffer):
    pass
