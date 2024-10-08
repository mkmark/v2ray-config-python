from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.features.stats as stats


@dataclass(slots=True)
class StatCouterConnection(Connection):
    readCounter: Optional[Counter] = field(default_factory=Counter)
    writeCounter: Optional[Counter] = field(default_factory=Counter)
