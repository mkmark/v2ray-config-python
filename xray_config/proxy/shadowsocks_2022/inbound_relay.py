from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.session as session
# import xray_config.common.singbridge as singbridge
# import xray_config.common.uuid as uuid
# import xray_config.features.routing as routing
# import xray_config.transport.internet.stat as stat


@dataclass(slots=True)
class RelayInbound:
    networks: Optional[list[str]] = field(default_factory=list[str])
    destinations: Optional[list[RelayDestination]] = field(default_factory=list[RelayDestination])
    service: Optional[RelayService[int]] = field(default_factory=RelayService[int])
