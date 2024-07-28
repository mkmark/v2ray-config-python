from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class TCPRequestHeader1PreSessionKey:
    salt: Optional[RequestSalt] = field(default_factory=RequestSalt)
    eIH: Optional[ExtensibleIdentityHeaders] = field(default_factory=ExtensibleIdentityHeaders)


@dataclass(slots=True)
class TCPRequestHeader2FixedLength:
    type: Optional[int] = None
    timestamp: Optional[int] = None
    headerLength: Optional[int] = None


@dataclass(slots=True)
class TCPRequestHeader3VariableLength(}):
    destinationAddress: Optional[DestinationAddress] = field(default_factory=DestinationAddress)
    contents: Optional[struct] = field(default_factory=struct)
    paddingLength: Optional[int] = None
    padding: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class TCPRequestHeader:
    preSessionKeyHeader: Optional[TCPRequestHeader1PreSessionKey] = field(default_factory=TCPRequestHeader1PreSessionKey)
    fixedLengthHeader: Optional[TCPRequestHeader2FixedLength] = field(default_factory=TCPRequestHeader2FixedLength)
    header: Optional[TCPRequestHeader3VariableLength] = field(default_factory=TCPRequestHeader3VariableLength)


@dataclass(slots=True)
class TCPResponseHeader1PreSessionKey:
    salt: Optional[RequestSalt] = field(default_factory=RequestSalt)


@dataclass(slots=True)
class TCPResponseHeader2FixedLength:
    type: Optional[int] = None
    timestamp: Optional[int] = None
    requestSalt: Optional[RequestSalt] = field(default_factory=RequestSalt)
    initialPayloadLength: Optional[int] = None


@dataclass(slots=True)
class TCPResponseHeader:
    preSessionKeyHeader: Optional[TCPResponseHeader1PreSessionKey] = field(default_factory=TCPResponseHeader1PreSessionKey)
    header: Optional[TCPResponseHeader2FixedLength] = field(default_factory=TCPResponseHeader2FixedLength)


@dataclass(slots=True)
class UDPRequest:
    sessionID: Optional[[8]byte] = field(default_factory=[8]byte)
    packetID: Optional[int] = None
    timeStamp: Optional[int] = None
    address: Optional[DestinationAddress] = field(default_factory=DestinationAddress)
    port: Optional[int] = None
    payload: Optional[Buffer] = field(default_factory=Buffer)


@dataclass(slots=True)
class UDPResponse(UDPRequest):
    clientSessionID: Optional[[8]byte] = field(default_factory=[8]byte)
