from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.features.routing as routing
# import v2ray_config.transport as transport


# @dataclass(slots=True)
# class packetConnectionAdaptor:
#     reader_access: Optional[Mutex] = field(default_factory=Mutex)
#     reader_buffer: Optional[MultiBuffer] = field(default_factory=MultiBuffer)
#     link: Optional[Link] = field(default_factory=Link)


# @dataclass(slots=True)
# class packetConnWrapper(PacketConn):
#     pass
