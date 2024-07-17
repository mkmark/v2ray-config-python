from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class ConfigCreatorCache(dict[str, ConfigCreator]):
    pass


@dataclass(slots=True)
class JSONConfigLoader:
    cache: Optional[ConfigCreatorCache] = field(default_factory=ConfigCreatorCache)
    id_key: Optional[str] = None
    config_key: Optional[str] = None
