from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors


@dataclass(slots=True)
class errorCollector:
    errors: Optional[Error] = field(default_factory=Error)
