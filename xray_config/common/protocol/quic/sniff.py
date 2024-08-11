from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.bytespool as bytespool
# import xray_config.common.errors as errors
# import xray_config.common.protocol.tls as tls


@dataclass(slots=True)
class SniffHeader:
    domain: Optional[str] = None
