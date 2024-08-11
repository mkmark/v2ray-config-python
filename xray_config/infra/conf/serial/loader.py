from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.core as core
# import xray_config.infra.conf as conf
# import xray_config.infra.conf.json as json


@dataclass(slots=True)
class offset:
    line: Optional[int] = None
    char: Optional[int] = None
