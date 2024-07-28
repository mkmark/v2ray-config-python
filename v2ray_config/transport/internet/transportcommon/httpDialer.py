from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet.security as security


@dataclass(slots=True)
class DialerFunc(Conn, error)):
    pass


@dataclass(slots=True)
class alpnAwareHTTPRoundTripperImpl:
    accessConnectWithH1: Optional[Mutex] = field(default_factory=Mutex)
    connectWithH1: Optional[dict[str, bool]] = field(default_factory=dict[str, bool])
    httpsH1Transport: Optional[RoundTripper] = field(default_factory=RoundTripper)
    httpsH2Transport: Optional[RoundTripper] = field(default_factory=RoundTripper)
    backdropTransport: Optional[RoundTripper] = field(default_factory=RoundTripper)
    accessDialingConnection: Optional[Mutex] = field(default_factory=Mutex)
    pendingConn: Optional[dict[pendingConnKey, unclaimedConnection]] = field(default_factory=dict[pendingConnKey, unclaimedConnection])
    ctx: Optional[Context] = field(default_factory=Context)
    dialer: Optional[DialerFunc] = field(default_factory=DialerFunc)


@dataclass(slots=True)
class pendingConnKey:
    isH2: Optional[bool] = None
    dest: Optional[str] = None


@dataclass(slots=True)
class unclaimedConnection(Conn):
    claimed: Optional[bool] = None
    access: Optional[Mutex] = field(default_factory=Mutex)
