from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.bytespool as bytespool
# import v2ray_config.common.errors as errors
# import v2ray_config.common.protocol.tls as tls


@dataclass(slots=True)
class SniffHeader:
    domain: Optional[str] = None
