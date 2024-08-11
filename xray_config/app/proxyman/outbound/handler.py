from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.proxyman as proxyman
# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.buf as buf
# import xray_config.common.mux as mux
# import xray_config.common.net as net
# import xray_config.common.net.cnc as cnc
# import xray_config.common.session as session
# import xray_config.core as core
# import xray_config.features.outbound as outbound
# import xray_config.features.policy as policy
# import xray_config.features.stats as stats
# import xray_config.proxy as proxy
# import xray_config.transport as transport
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls
# import xray_config.transport.pipe as pipe


@dataclass(slots=True)
class Handler:
    tag: Optional[str] = None
    senderSettings: Optional[SenderConfig] = field(default_factory=SenderConfig)
    streamSettings: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
    proxy: Optional[Outbound] = field(default_factory=Outbound)
    outboundManager: Optional[Manager] = field(default_factory=Manager)
    mux: Optional[ClientManager] = field(default_factory=ClientManager)
    xudp: Optional[ClientManager] = field(default_factory=ClientManager)
    udp443: Optional[str] = None
    uplinkCounter: Optional[Counter] = field(default_factory=Counter)
    downlinkCounter: Optional[Counter] = field(default_factory=Counter)
