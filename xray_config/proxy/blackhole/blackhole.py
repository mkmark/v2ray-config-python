from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.session as session
# import xray_config.transport as transport
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class Handler:
    response: Optional[ResponseConfig] = field(default_factory=ResponseConfig)
