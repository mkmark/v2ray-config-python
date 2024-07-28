from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.subscription as subscription
# import v2ray_config.app.subscription.containers as containers
# import v2ray_config.app.subscription.specs as specs


@dataclass(slots=True)
class trackedSubscription:
    importSource: Optional[ImportSource] = field(default_factory=ImportSource)
    currentDocumentExpireTime: Optional[Time] = field(default_factory=Time)
    currentDocument: Optional[SubscriptionDocument] = field(default_factory=SubscriptionDocument)
    materialized: Optional[dict[str, materializedServer]] = field(default_factory=dict[str, materializedServer])
    originalDocument: Optional[list[int]] = field(default_factory=list[int])
    originalContainer: Optional[Container] = field(default_factory=Container)
    originalServerConfig: Optional[dict[str, originalServerConfig]] = field(default_factory=dict[str, originalServerConfig])


@dataclass(slots=True)
class originalServerConfig:
    data: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class materializedServer:
    tagPostfix: Optional[str] = None
    serverConfig: Optional[SubscriptionServerConfig] = field(default_factory=SubscriptionServerConfig)
