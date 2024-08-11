from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.cmdarg as cmdarg
# import xray_config.common.errors as errors
# import xray_config.main.confloader as confloader


@dataclass(slots=True)
class ConfigBuilder(func(files []string, formats []string) (*Config, error)):
    pass


@dataclass(slots=True)
class ConfigsMerger(func(files []string, formats []string) (string, error)):
    pass


@dataclass(slots=True)
class ConfigFormat:
    name: Optional[str] = None
    extension: Optional[list[str]] = field(default_factory=list[str])
    loader: Optional[ConfigLoader] = field(default_factory=ConfigLoader)
