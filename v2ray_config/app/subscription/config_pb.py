from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class ImportSource:
    name: Optional[str] = None
    url: Optional[str] = None
    tag_prefix: Optional[str] = None
    import_using_tag: Optional[str] = None
    default_expire_seconds: Optional[int] = None


@dataclass(slots=True)
class Config:
    imports: Optional[list[ImportSource]] = field(default_factory=list[ImportSource])
    nonnative_converter_overlay: Optional[list[int]] = field(default_factory=list[int])
    nonnative_converter_overlay_file: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
