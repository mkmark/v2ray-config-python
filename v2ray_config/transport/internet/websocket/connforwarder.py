from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class connectionForwarder(ReadWriteCloser):
    shouldWait: Optional[bool] = None
    delayedDialFinish: Optional[Context] = field(default_factory=Context)
    finishedDial: Optional[CancelFunc] = field(default_factory=CancelFunc)
    dialer: Optional[DelayedDialerForwarded] = field(default_factory=DelayedDialerForwarded)
