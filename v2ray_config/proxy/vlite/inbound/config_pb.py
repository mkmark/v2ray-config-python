from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class UDPProtocolConfig:
    password: Optional[str] = None
    scramble_packet: Optional[bool] = None
    enable_fec: Optional[bool] = None
    enable_stabilization: Optional[bool] = None
    enable_renegotiation: Optional[bool] = None
    handshake_masking_padding_size: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
