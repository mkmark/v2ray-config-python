from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class ListInstanceReq:
    pass


@dataclass(slots=True)
class ListInstanceResp:
    name: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class AddInstanceReq:
    name: Optional[str] = None
    config_type: Optional[str] = None
    config_content_b64: Optional[str] = None


@dataclass(slots=True)
class AddInstanceResp:
    pass


@dataclass(slots=True)
class StartInstanceReq:
    name: Optional[str] = None


@dataclass(slots=True)
class StartInstanceResp:
    pass


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class x:
    pass
