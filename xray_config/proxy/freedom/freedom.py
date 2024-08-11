from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.dice as dice
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.platform as platform
# import xray_config.common.retry as retry
# import xray_config.common.session as session
# import xray_config.common.signal as signal
# import xray_config.common.task as task
# import xray_config.core as core
# import xray_config.features.dns as dns
# import xray_config.features.policy as policy
# import xray_config.features.stats as stats
# import xray_config.proxy as proxy
# import xray_config.transport as transport
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Handler:
    policyManager: Optional[Manager] = field(default_factory=Manager)
    dns: Optional[Client] = field(default_factory=Client)
    config: Optional[Config] = field(default_factory=Config)


@dataclass(slots=True)
class PacketReader(PacketConnWrapper, Counter):
    pass


@dataclass(slots=True)
class PacketWriter(PacketConnWrapper, Counter, Handler, Context):
    uDPOverride: Optional[Destination] = field(default_factory=Destination)


@dataclass(slots=True)
class FragmentWriter:
    fragment: Optional[Fragment] = field(default_factory=Fragment)
    writer: Optional[Writer] = field(default_factory=Writer)
    count: Optional[int] = None
