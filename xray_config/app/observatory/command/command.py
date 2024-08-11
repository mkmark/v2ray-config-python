from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.observatory as observatory
# import xray_config.common as common
# import xray_config.core as core
# import xray_config.features.extension as extension


@dataclass(slots=True)
class service(UnimplementedObservatoryServiceServer):
    v: Optional[Instance] = field(default_factory=Instance)
    observatory: Optional[Observatory] = field(default_factory=Observatory)
