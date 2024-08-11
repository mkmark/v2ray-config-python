from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.browser_dialer as browser_dialer
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class delayDialConn(Conn):
    closed: Optional[bool] = None
    dialed: Optional[chan] = field(default_factory=chan)
    cancel: Optional[CancelFunc] = field(default_factory=CancelFunc)
    ctx: Optional[Context] = field(default_factory=Context)
    dest: Optional[Destination] = field(default_factory=Destination)
    streamSettings: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
