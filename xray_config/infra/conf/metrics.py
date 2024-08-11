from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.metrics as metrics
# import xray_config.common.errors as errors


@dataclass(slots=True)
class MetricsConfig:
    tag: Optional[str] = None
