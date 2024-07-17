from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.errors as errors


@dataclass(slots=True)
class UUID([16]byte):
    pass
