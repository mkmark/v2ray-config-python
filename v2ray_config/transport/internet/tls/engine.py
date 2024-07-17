from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.transport.internet.security as security


@dataclass(slots=True)
class Engine:
    config: Optional[Config] = field(default_factory=Config)
