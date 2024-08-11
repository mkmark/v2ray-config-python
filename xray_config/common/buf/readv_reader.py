from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.platform as platform
# import xray_config.features.stats as stats


@dataclass(slots=True)
class allocStrategy:
    current: Optional[int] = None


@dataclass(slots=True)
class ReadVReader(Reader):
    rawConn: Optional[RawConn] = field(default_factory=RawConn)
    mr: Optional[multiReader] = field(default_factory=multiReader)
    alloc: Optional[allocStrategy] = field(default_factory=allocStrategy)
    counter: Optional[Counter] = field(default_factory=Counter)
