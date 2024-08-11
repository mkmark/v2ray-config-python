from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.transport.internet.headers.dns as dns
# import xray_config.transport.internet.headers.http as http
# import xray_config.transport.internet.headers.noop as noop
# import xray_config.transport.internet.headers.srtp as srtp
# import xray_config.transport.internet.headers.tls as tls
# import xray_config.transport.internet.headers.utp as utp
# import xray_config.transport.internet.headers.wechat as wechat
# import xray_config.transport.internet.headers.wireguard as wireguard


@dataclass(slots=True)
class NoOpAuthenticator:
    pass


@dataclass(slots=True)
class NoOpConnectionAuthenticator:
    pass


@dataclass(slots=True)
class SRTPAuthenticator:
    pass


@dataclass(slots=True)
class UTPAuthenticator:
    pass


@dataclass(slots=True)
class WechatVideoAuthenticator:
    pass


@dataclass(slots=True)
class WireguardAuthenticator:
    pass


@dataclass(slots=True)
class DNSAuthenticator:
    domain: Optional[str] = None


@dataclass(slots=True)
class DTLSAuthenticator:
    pass


@dataclass(slots=True)
class AuthenticatorRequest:
    version: Optional[str] = None
    method: Optional[str] = None
    path: Optional[list[str]] = field(default_factory=list[str])
    headers: Optional[dict[str, list[str]]] = field(default_factory=dict[str, list[str]])


@dataclass(slots=True)
class AuthenticatorResponse:
    version: Optional[str] = None
    status: Optional[str] = None
    reason: Optional[str] = None
    headers: Optional[dict[str, list[str]]] = field(default_factory=dict[str, list[str]])


@dataclass(slots=True)
class Authenticator:
    request: Optional[AuthenticatorRequest] = field(default_factory=AuthenticatorRequest)
    response: Optional[AuthenticatorResponse] = field(default_factory=AuthenticatorResponse)
