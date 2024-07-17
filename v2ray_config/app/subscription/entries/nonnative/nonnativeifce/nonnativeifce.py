from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.subscription.entries as entries


@dataclass(slots=True)
class NonNativeConverterConstructorT(Converter, error)):
    pass
