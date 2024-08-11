from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.features.stats as stats


@dataclass(slots=True)
class CounterConnection(Connection):
    readCounter: Optional[Counter] = field(default_factory=Counter)
    writeCounter: Optional[Counter] = field(default_factory=Counter)
