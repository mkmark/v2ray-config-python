from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class connectionForwarder(ReadWriteCloser):
    should_wait: Optional[bool] = None
    delayed_dial_finish: Optional[Context] = field(default_factory=Context)
    finished_dial: Optional[CancelFunc] = field(default_factory=CancelFunc)
    dialer: Optional[DelayedDialerForwarded] = field(default_factory=DelayedDialerForwarded)
