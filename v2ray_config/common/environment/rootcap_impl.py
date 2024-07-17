from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.platform.filesystem.fsifce as fsifce
# import v2ray_config.features.extension.storage as storage
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tagged as tagged


@dataclass(slots=True)
class rootEnvImpl:
    transient_storage: Optional[ScopedTransientStorage] = field(default_factory=ScopedTransientStorage)
    system_dialer: Optional[SystemDialer] = field(default_factory=SystemDialer)
    system_listener: Optional[SystemListener] = field(default_factory=SystemListener)
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class appEnvImpl:
    transient_storage: Optional[ScopedTransientStorage] = field(default_factory=ScopedTransientStorage)
    system_dialer: Optional[SystemDialer] = field(default_factory=SystemDialer)
    system_listener: Optional[SystemListener] = field(default_factory=SystemListener)
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class proxyEnvImpl:
    transient_storage: Optional[ScopedTransientStorage] = field(default_factory=ScopedTransientStorage)
    system_dialer: Optional[SystemDialer] = field(default_factory=SystemDialer)
    system_listener: Optional[SystemListener] = field(default_factory=SystemListener)
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class transportEnvImpl:
    transient_storage: Optional[ScopedTransientStorage] = field(default_factory=ScopedTransientStorage)
    system_dialer: Optional[SystemDialer] = field(default_factory=SystemDialer)
    system_listener: Optional[SystemListener] = field(default_factory=SystemListener)
    ctx: Optional[Context] = field(default_factory=Context)
