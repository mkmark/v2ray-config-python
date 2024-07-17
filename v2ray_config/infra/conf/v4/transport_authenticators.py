from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.transport.internet.headers.http as http
# import v2ray_config.transport.internet.headers.noop as noop
# import v2ray_config.transport.internet.headers.srtp as srtp
# import v2ray_config.transport.internet.headers.tls as tls
# import v2ray_config.transport.internet.headers.utp as utp
# import v2ray_config.transport.internet.headers.wechat as wechat
# import v2ray_config.transport.internet.headers.wireguard as wireguard


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
