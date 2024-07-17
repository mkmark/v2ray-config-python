from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.platform as platform


@dataclass(slots=True)
class allocStrategy:
    current: Optional[int] = None


@dataclass(slots=True)
class ReadVReader(Reader):
    raw_conn: Optional[RawConn] = field(default_factory=RawConn)
    mr: Optional[multiReader] = field(default_factory=multiReader)
    alloc: Optional[allocStrategy] = field(default_factory=allocStrategy)
