from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.log as log


@dataclass(slots=True)
class HandlerCreator(Handler, error)):
    pass


@dataclass(slots=True)
class HandlerCreatorOptions:
    path: Optional[str] = None
