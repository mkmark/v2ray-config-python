from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.signal as signal
# import v2ray_config.common.signal.semaphore as semaphore


@dataclass(slots=True)
class State(int):
    pass


@dataclass(slots=True)
class RoundTripInfo(RWMutex):
    variation: Optional[int] = None
    srtt: Optional[int] = None
    rto: Optional[int] = None
    minRtt: Optional[int] = None
    updatedTimestamp: Optional[int] = None


@dataclass(slots=True)
class Updater:
    interval: Optional[int] = None
    notifier: Optional[Instance] = field(default_factory=Instance)


@dataclass(slots=True)
class ConnMetadata:
    localAddr: Optional[Addr] = field(default_factory=Addr)
    remoteAddr: Optional[Addr] = field(default_factory=Addr)
    conversation: Optional[int] = None


@dataclass(slots=True)
class Connection:
    meta: Optional[ConnMetadata] = field(default_factory=ConnMetadata)
    closer: Optional[Closer] = field(default_factory=Closer)
    rd: Optional[Time] = field(default_factory=Time)
    wd: Optional[Time] = field(default_factory=Time)
    since: Optional[int] = None
    dataInput: Optional[Notifier] = field(default_factory=Notifier)
    dataOutput: Optional[Notifier] = field(default_factory=Notifier)
    config: Optional[Config] = field(default_factory=Config)
    stateBeginTime: Optional[int] = None
    lastIncomingTime: Optional[int] = None
    lastPingTime: Optional[int] = None
    mss: Optional[int] = None
    roundTrip: Optional[RoundTripInfo] = field(default_factory=RoundTripInfo)
    receivingWorker: Optional[ReceivingWorker] = field(default_factory=ReceivingWorker)
    sendingWorker: Optional[SendingWorker] = field(default_factory=SendingWorker)
    output: Optional[SegmentWriter] = field(default_factory=SegmentWriter)
    dataUpdater: Optional[Updater] = field(default_factory=Updater)
    pingUpdater: Optional[Updater] = field(default_factory=Updater)
