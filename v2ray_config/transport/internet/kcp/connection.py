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
    min_rtt: Optional[int] = None
    updated_timestamp: Optional[int] = None


@dataclass(slots=True)
class Updater:
    interval: Optional[int] = None
    notifier: Optional[Instance] = field(default_factory=Instance)


@dataclass(slots=True)
class ConnMetadata:
    local_addr: Optional[Addr] = field(default_factory=Addr)
    remote_addr: Optional[Addr] = field(default_factory=Addr)
    conversation: Optional[int] = None


@dataclass(slots=True)
class Connection:
    meta: Optional[ConnMetadata] = field(default_factory=ConnMetadata)
    closer: Optional[Closer] = field(default_factory=Closer)
    rd: Optional[Time] = field(default_factory=Time)
    wd: Optional[Time] = field(default_factory=Time)
    since: Optional[int] = None
    data_input: Optional[Notifier] = field(default_factory=Notifier)
    data_output: Optional[Notifier] = field(default_factory=Notifier)
    config: Optional[Config] = field(default_factory=Config)
    state_begin_time: Optional[int] = None
    last_incoming_time: Optional[int] = None
    last_ping_time: Optional[int] = None
    mss: Optional[int] = None
    round_trip: Optional[RoundTripInfo] = field(default_factory=RoundTripInfo)
    receiving_worker: Optional[ReceivingWorker] = field(default_factory=ReceivingWorker)
    sending_worker: Optional[SendingWorker] = field(default_factory=SendingWorker)
    output: Optional[SegmentWriter] = field(default_factory=SegmentWriter)
    data_updater: Optional[Updater] = field(default_factory=Updater)
    ping_updater: Optional[Updater] = field(default_factory=Updater)
