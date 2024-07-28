from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.subscription as subscription
# import v2ray_config.app.subscription.entries as entries
# import v2ray_config.app.subscription.entries.nonnative.nonnativeifce as nonnativeifce
# import v2ray_config.common as common
# import v2ray_config.common.task as task
# import v2ray_config.features.extension as extension


@dataclass(slots=True)
class SubscriptionManagerImpl:
    config: Optional[Config] = field(default_factory=Config)
    ctx: Optional[Context] = field(default_factory=Context)
    s: Optional[Instance] = field(default_factory=Instance)
    converter: Optional[ConverterRegistry] = field(default_factory=ConverterRegistry)
    trackedSubscriptions: Optional[dict[str, trackedSubscription]] = field(default_factory=dict[str, trackedSubscription])
    refreshTask: Optional[Periodic] = field(default_factory=Periodic)
