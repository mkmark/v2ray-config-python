from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class MTU:
    value: Optional[int] = None


@dataclass(slots=True)
class TTI:
    value: Optional[int] = None


@dataclass(slots=True)
class UplinkCapacity:
    value: Optional[int] = None


@dataclass(slots=True)
class DownlinkCapacity:
    value: Optional[int] = None


@dataclass(slots=True)
class WriteBuffer:
    size: Optional[int] = None


@dataclass(slots=True)
class ReadBuffer:
    size: Optional[int] = None


@dataclass(slots=True)
class ConnectionReuse:
    enable: Optional[bool] = None


@dataclass(slots=True)
class EncryptionSeed:
    seed: Optional[str] = None


@dataclass(slots=True)
class Config:
    mtu: Optional[MTU] = field(default_factory=MTU)
    tti: Optional[TTI] = field(default_factory=TTI)
    uplink_capacity: Optional[UplinkCapacity] = field(default_factory=UplinkCapacity)
    downlink_capacity: Optional[DownlinkCapacity] = field(default_factory=DownlinkCapacity)
    congestion: Optional[bool] = None
    write_buffer: Optional[WriteBuffer] = field(default_factory=WriteBuffer)
    read_buffer: Optional[ReadBuffer] = field(default_factory=ReadBuffer)
    header_config: Optional[Any] = field(default_factory=Any)
    seed: Optional[EncryptionSeed] = field(default_factory=EncryptionSeed)


@dataclass(slots=True)
class x:
    pass
