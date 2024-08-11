from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net
# import xray_config.features.routing as routing


@dataclass(slots=True)
class routingContext(RoutingContext):
    pass
