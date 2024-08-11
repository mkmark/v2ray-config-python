from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.observatory as observatory
# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.core as core
# import xray_config.features.extension as extension


@dataclass(slots=True)
class outboundList(list[str]):
    pass


@dataclass(slots=True)
class LeastPingStrategy:
    # ctx: Optional[Context] = field(default_factory=Context)
    # observatory: Optional[Observatory] = field(default_factory=Observatory)
    pass
