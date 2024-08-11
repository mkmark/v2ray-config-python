from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.observatory as observatory
# import xray_config.common as common
# import xray_config.common.dice as dice
# import xray_config.core as core
# import xray_config.features.extension as extension


@dataclass(slots=True)
class RandomStrategy:
    fallbackTag: Optional[str] = None
    ctx: Optional[Context] = field(default_factory=Context)
    observatory: Optional[Observatory] = field(default_factory=Observatory)
