from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.features.routing as routing


@dataclass(slots=True)
class routingContext(RoutingContext):
    pass
