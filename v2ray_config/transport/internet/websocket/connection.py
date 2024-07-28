from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.errors as errors
# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class connection:
    conn: Optional[Conn] = field(default_factory=Conn)
    reader: Optional[Reader] = field(default_factory=Reader)
    remoteAddr: Optional[Addr] = field(default_factory=Addr)
    shouldWait: Optional[bool] = None
    delayedDialFinish: Optional[Context] = field(default_factory=Context)
    finishedDial: Optional[CancelFunc] = field(default_factory=CancelFunc)
    dialer: Optional[DelayedDialer] = field(default_factory=DelayedDialer)
