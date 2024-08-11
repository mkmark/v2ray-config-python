from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.signal as signal
# import xray_config.common.signal.done as done


@dataclass(slots=True)
class state(int):
    pass


@dataclass(slots=True)
class pipeOption:
    limit: Optional[int] = None
    discardOverflow: Optional[bool] = None


@dataclass(slots=True)
class pipe(Mutex):
    data: Optional[MultiBuffer] = field(default_factory=MultiBuffer)
    readSignal: Optional[Notifier] = field(default_factory=Notifier)
    writeSignal: Optional[Notifier] = field(default_factory=Notifier)
    done: Optional[Instance] = field(default_factory=Instance)
    errChan: Optional[chan] = field(default_factory=chan)
    option: Optional[pipeOption] = field(default_factory=pipeOption)
