from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.subscription.entries as entries
# import v2ray_config.app.subscription.entries.nonnative.nonnativeifce as nonnativeifce
# import v2ray_config.app.subscription.entries.outbound as outbound
# import v2ray_config.app.subscription.specs as specs
# import v2ray_config.common as common


@dataclass(slots=True)
class nonNativeConverter:
    matcher: Optional[DefMatcher] = field(default_factory=DefMatcher)
