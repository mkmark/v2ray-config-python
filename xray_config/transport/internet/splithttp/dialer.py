from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.signal.semaphore as semaphore
# import xray_config.common.uuid as uuid
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.browser_dialer as browser_dialer
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls
# import xray_config.transport.pipe as pipe


@dataclass(slots=True)
class dialerConf(Destination, MemoryStreamConfig):
    pass
