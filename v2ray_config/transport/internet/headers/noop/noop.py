from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common


@dataclass(slots=True)
class Header:
    pass


@dataclass(slots=True)
class ConnectionHeader:
    pass
