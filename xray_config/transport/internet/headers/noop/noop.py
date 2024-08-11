from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common


@dataclass(slots=True)
class NoOpHeader:
    pass


@dataclass(slots=True)
class NoOpConnectionHeader:
    pass
