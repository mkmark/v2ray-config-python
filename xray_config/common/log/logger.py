from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.platform as platform
# import xray_config.common.signal.done as done
# import xray_config.common.signal.semaphore as semaphore


@dataclass(slots=True)
class WriterCreator(func() Writer):
    pass


@dataclass(slots=True)
class generalLogger:
    creator: Optional[WriterCreator] = field(default_factory=WriterCreator)
    buffer: Optional[chan] = field(default_factory=chan)
    access: Optional[Instance] = field(default_factory=Instance)
    done: Optional[Instance] = field(default_factory=Instance)


@dataclass(slots=True)
class serverityLogger:
    inner: Optional[generalLogger] = field(default_factory=generalLogger)
    logLevel: Optional[Severity] = field(default_factory=Severity)


@dataclass(slots=True)
class consoleLogWriter:
    logger: Optional[Logger] = field(default_factory=Logger)


@dataclass(slots=True)
class fileLogWriter:
    file: Optional[File] = field(default_factory=File)
    logger: Optional[Logger] = field(default_factory=Logger)
