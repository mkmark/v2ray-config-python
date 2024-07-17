from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.subscription.specs as specs


@dataclass(slots=True)
class ConverterRegistry:
    known_converters: Optional[dict[str, Converter]] = field(default_factory=dict[str, Converter])
    parent: Optional[ConverterRegistry] = field(default_factory=ConverterRegistry)
