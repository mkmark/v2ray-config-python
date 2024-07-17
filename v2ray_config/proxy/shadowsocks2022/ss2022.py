from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol


# @dataclass(slots=True)
# class TCPRequestHeader1PreSessionKey:
#     salt: Optional[RequestSalt] = field(default_factory=RequestSalt)
#     eih: Optional[ExtensibleIdentityHeaders] = field(default_factory=ExtensibleIdentityHeaders)


# @dataclass(slots=True)
# class TCPRequestHeader2FixedLength:
#     type: Optional[int] = None
#     timestamp: Optional[int] = None
#     header_length: Optional[int] = None


# @dataclass(slots=True)
# class TCPRequestHeader3VariableLength(}):
#     destination_address: Optional[DestinationAddress] = field(default_factory=DestinationAddress)
#     contents: Optional[struct] = field(default_factory=struct)
#     padding_length: Optional[int] = None
#     padding: Optional[list[int]] = field(default_factory=list[int])


# @dataclass(slots=True)
# class TCPRequestHeader:
#     pre_session_key_header: Optional[TCPRequestHeader1PreSessionKey] = field(default_factory=TCPRequestHeader1PreSessionKey)
#     fixed_length_header: Optional[TCPRequestHeader2FixedLength] = field(default_factory=TCPRequestHeader2FixedLength)
#     header: Optional[TCPRequestHeader3VariableLength] = field(default_factory=TCPRequestHeader3VariableLength)


# @dataclass(slots=True)
# class TCPResponseHeader1PreSessionKey:
#     salt: Optional[RequestSalt] = field(default_factory=RequestSalt)


# @dataclass(slots=True)
# class TCPResponseHeader2FixedLength:
#     type: Optional[int] = None
#     timestamp: Optional[int] = None
#     request_salt: Optional[RequestSalt] = field(default_factory=RequestSalt)
#     initial_payload_length: Optional[int] = None


# @dataclass(slots=True)
# class TCPResponseHeader:
#     pre_session_key_header: Optional[TCPResponseHeader1PreSessionKey] = field(default_factory=TCPResponseHeader1PreSessionKey)
#     header: Optional[TCPResponseHeader2FixedLength] = field(default_factory=TCPResponseHeader2FixedLength)


# @dataclass(slots=True)
# class UDPRequest:
#     session_id: Optional[[8]byte] = field(default_factory=[8]byte)
#     packet_id: Optional[int] = None
#     time_stamp: Optional[int] = None
#     address: Optional[DestinationAddress] = field(default_factory=DestinationAddress)
#     port: Optional[int] = None
#     payload: Optional[Buffer] = field(default_factory=Buffer)


# @dataclass(slots=True)
# class UDPResponse(UDPRequest):
#     client_session_id: Optional[[8]byte] = field(default_factory=[8]byte)
