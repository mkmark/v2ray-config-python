from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet.security as security


@dataclass(slots=True)
class DialerFunc(Conn, error)):
    pass


@dataclass(slots=True)
class alpnAwareHTTPRoundTripperImpl:
    access_connect_with_h1: Optional[Mutex] = field(default_factory=Mutex)
    connect_with_h1: Optional[dict[str, bool]] = field(default_factory=dict[str, bool])
    https_h1_transport: Optional[RoundTripper] = field(default_factory=RoundTripper)
    https_h2_transport: Optional[RoundTripper] = field(default_factory=RoundTripper)
    backdrop_transport: Optional[RoundTripper] = field(default_factory=RoundTripper)
    access_dialing_connection: Optional[Mutex] = field(default_factory=Mutex)
    pending_conn: Optional[dict[pendingConnKey, unclaimedConnection]] = field(default_factory=dict[pendingConnKey, unclaimedConnection])
    ctx: Optional[Context] = field(default_factory=Context)
    dialer: Optional[DialerFunc] = field(default_factory=DialerFunc)


@dataclass(slots=True)
class pendingConnKey:
    is_h2: Optional[bool] = None
    dest: Optional[str] = None


@dataclass(slots=True)
class unclaimedConnection(Conn):
    claimed: Optional[bool] = None
    access: Optional[Mutex] = field(default_factory=Mutex)
