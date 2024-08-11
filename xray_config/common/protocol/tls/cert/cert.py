from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors


@dataclass(slots=True)
class Option(Certificate)):
    pass


@dataclass(slots=True)
class Certificate:
    certificate: Optional[list[int]] = field(default_factory=list[int])
    privateKey: Optional[list[int]] = field(default_factory=list[int])
