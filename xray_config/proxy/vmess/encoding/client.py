from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.bitmask as bitmask
# import xray_config.common.buf as buf
# import xray_config.common.crypto as crypto
# import xray_config.common.dice as dice
# import xray_config.common.drain as drain
# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol
# import xray_config.proxy.vmess as vmess
# import xray_config.proxy.vmess.aead as aead


@dataclass(slots=True)
class ClientSession:
    requestBodyKey: Optional[[16]byte] = field(default_factory=[16]byte)
    requestBodyIV: Optional[[16]byte] = field(default_factory=[16]byte)
    responseBodyKey: Optional[[16]byte] = field(default_factory=[16]byte)
    responseBodyIV: Optional[[16]byte] = field(default_factory=[16]byte)
    responseReader: Optional[Reader] = field(default_factory=Reader)
    responseHeader: Optional[int] = None
    readDrainer: Optional[Drainer] = field(default_factory=Drainer)
