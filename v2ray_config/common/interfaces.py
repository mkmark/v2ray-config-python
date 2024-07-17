from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.errors as errors


@dataclass(slots=True)
class ChainedClosable(list[Closable]):
    pass
