from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext
import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class ForcedALPN(int):
    pass


@dataclass(slots=True)
class Config:
    tls_config: Optional[tls.config_pb.Config] = field(
        default_factory=tls.config_pb.Config
    )
    imitate: Optional[str] = None
    noSNI: Optional[bool] = None
    force_alpn: Optional[ForcedALPN] = field(default_factory=ForcedALPN)


@dataclass(slots=True)
class x:
    pass
