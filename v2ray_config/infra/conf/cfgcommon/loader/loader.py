from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class ConfigCreatorCache(dict[str, ConfigCreator]):
    pass


@dataclass(slots=True)
class JSONConfigLoader:
    cache: Optional[ConfigCreatorCache] = field(default_factory=ConfigCreatorCache)
    idKey: Optional[str] = None
    configKey: Optional[str] = None
