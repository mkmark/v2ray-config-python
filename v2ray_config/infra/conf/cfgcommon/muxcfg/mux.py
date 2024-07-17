from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.proxyman as proxyman


@dataclass(slots=True)
class MuxConfig:
    enabled: Optional[bool] = None
    concurrency: Optional[int] = None
