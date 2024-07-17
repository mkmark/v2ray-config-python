from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.errors as errors
# import v2ray_config.infra.conf.json as json
# import v2ray_config.infra.conf.v4 as v4


@dataclass(slots=True)
class offset:
    line: Optional[int] = None
    char: Optional[int] = None
