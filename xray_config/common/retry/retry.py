from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.retry as retry
# import xray_config.common.errors as errors


@dataclass(slots=True)
class retryer:
    totalAttempt: Optional[int] = None
