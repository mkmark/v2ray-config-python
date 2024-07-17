from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.bytespool as bytespool
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.retry as retry
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.task as task
# import v2ray_config.features.policy as policy
# import v2ray_config.proxy as proxy
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tls as tls


# @dataclass(slots=True)
# class Client:
#     server_picker: Optional[ServerPicker] = field(default_factory=ServerPicker)
#     policy_manager: Optional[Manager] = field(default_factory=Manager)
#     h_1_skip_wait_for_reply: Optional[bool] = None


# @dataclass(slots=True)
# class h2Conn:
#     raw_conn: Optional[Conn] = field(default_factory=Conn)
#     h_2_conn: Optional[ClientConn] = field(default_factory=ClientConn)


# @dataclass(slots=True)
# class http2Conn(Conn):
#     in: Optional[PipeWriter] = field(default_factory=PipeWriter)
#     out: Optional[ReadCloser] = field(default_factory=ReadCloser)
