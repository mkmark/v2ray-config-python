from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.uuid as uuid
# import xray_config.common as common
# import xray_config.common.errors as errors


@dataclass(slots=True)
class UUID([16]byte):
    pass
