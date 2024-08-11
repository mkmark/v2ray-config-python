from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.ctx as ctx
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.net.cnc as cnc
# import xray_config.common.session as session
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.reality as reality
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls
# import xray_config.transport.pipe as pipe


@dataclass(slots=True)
class dialerConf(Destination, MemoryStreamConfig):
    pass


@dataclass(slots=True)
class WaitReadCloser(ReadCloser):
    wait: Optional[chan] = field(default_factory=chan)
