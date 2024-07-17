from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.platform as platform
# import v2ray_config.common.platform.filesystem as filesystem


@dataclass(slots=True)
class EmbeddedHashProtectedLoader:
    checked_file: Optional[dict[str, str]] = field(default_factory=dict[str, str])
