from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.subscription as subscription
# import v2ray_config.app.subscription.containers as containers
# import v2ray_config.app.subscription.specs as specs


@dataclass(slots=True)
class trackedSubscription:
    import_source: Optional[ImportSource] = field(default_factory=ImportSource)
    current_document_expire_time: Optional[Time] = field(default_factory=Time)
    current_document: Optional[SubscriptionDocument] = field(default_factory=SubscriptionDocument)
    materialized: Optional[dict[str, materializedServer]] = field(default_factory=dict[str, materializedServer])
    original_document: Optional[list[int]] = field(default_factory=list[int])
    original_container: Optional[Container] = field(default_factory=Container)
    original_server_config: Optional[dict[str, originalServerConfig]] = field(default_factory=dict[str, originalServerConfig])


@dataclass(slots=True)
class originalServerConfig:
    data: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class materializedServer:
    tag_postfix: Optional[str] = None
    server_config: Optional[SubscriptionServerConfig] = field(default_factory=SubscriptionServerConfig)
