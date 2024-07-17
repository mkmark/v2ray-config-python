from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.features.extension.storage as storage


@dataclass(slots=True)
class scopedTransientStorageImpl:
    access: Optional[Mutex] = field(default_factory=Mutex)
    scopes: Optional[dict[str, ScopedTransientStorage]] = field(default_factory=dict[str, ScopedTransientStorage])
    values: Optional[dict[str, dict]] = field(default_factory=dict[str, dict])
