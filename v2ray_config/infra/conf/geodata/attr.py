from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.router.routercommon as routercommon


@dataclass(slots=True)
class BooleanMatcher(str):
    pass


@dataclass(slots=True)
class AttributeList:
    matcher: Optional[list[AttributeMatcher]] = field(default_factory=list[AttributeMatcher])
