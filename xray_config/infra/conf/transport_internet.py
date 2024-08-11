from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.infra.conf.common import Int32Range
from xray_config.infra.conf.grpc import GRPCConfig

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.platform.filesystem as filesystem
# import xray_config.common.protocol as protocol
# import xray_config.common.serial as serial
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.domainsocket as domainsocket
# import xray_config.transport.internet.headers.http as http
# import xray_config.transport.internet.http as http
# import xray_config.transport.internet.httpupgrade as httpupgrade
# import xray_config.transport.internet.kcp as kcp
# import xray_config.transport.internet.quic as quic
# import xray_config.transport.internet.reality as reality
# import xray_config.transport.internet.splithttp as splithttp
# import xray_config.transport.internet.tcp as tcp
# import xray_config.transport.internet.tls as tls
# import xray_config.transport.internet.websocket as websocket


@dataclass(slots=True)
class TransportProtocol(str):
    pass


@dataclass(slots=True)
class KCPConfig:
    mtu: Optional[int] = None
    tti: Optional[int] = None
    uplinkCapacity: Optional[int] = None
    downlinkCapacity: Optional[int] = None
    congestion: Optional[bool] = None
    readBufferSize: Optional[int] = None
    writeBufferSize: Optional[int] = None
    header: Optional[dict] = field(default_factory=dict)
    seed: Optional[str] = None


@dataclass(slots=True)
class TCPConfig:
    header: Optional[dict] = field(default_factory=dict)
    acceptProxyProtocol: Optional[bool] = None


@dataclass(slots=True)
class WebSocketConfig:
    host: Optional[str] = None
    path: Optional[str] = None
    headers: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    acceptProxyProtocol: Optional[bool] = None


@dataclass(slots=True)
class HttpUpgradeConfig:
    host: Optional[str] = None
    path: Optional[str] = None
    headers: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    acceptProxyProtocol: Optional[bool] = None


@dataclass(slots=True)
class SplitHTTPConfig:
    host: Optional[str] = None
    path: Optional[str] = None
    headers: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    scMaxConcurrentPosts: Optional[Int32Range] = field(default_factory=Int32Range)
    scMaxEachPostBytes: Optional[Int32Range] = field(default_factory=Int32Range)
    scMinPostsIntervalMs: Optional[Int32Range] = field(default_factory=Int32Range)
    noSSEHeader: Optional[bool] = None
    responseOkPadding: Optional[Int32Range] = field(default_factory=Int32Range)


@dataclass(slots=True)
class HTTPConfig:
    host: Optional[list[str]] = field(default_factory=list[str])
    path: Optional[str] = None
    read_idle_timeout: Optional[int] = None
    health_check_timeout: Optional[int] = None
    method: Optional[str] = None
    headers: Optional[dict[str, list[str]]] = field(
        default_factory=dict[str, list[str]]
    )


@dataclass(slots=True)
class QUICConfig:
    header: Optional[dict] = field(default_factory=dict)
    security: Optional[str] = None
    key: Optional[str] = None


@dataclass(slots=True)
class DomainSocketConfig:
    path: Optional[str] = None
    abstract: Optional[bool] = None
    padding: Optional[bool] = None


@dataclass(slots=True)
class TLSCertConfig:
    certificateFile: Optional[str] = None
    certificate: Optional[list[str]] = field(default_factory=list[str])
    keyFile: Optional[str] = None
    key: Optional[list[str]] = field(default_factory=list[str])
    usage: Optional[str] = None
    ocspStapling: Optional[int] = None
    oneTimeLoading: Optional[bool] = None
    buildChain: Optional[bool] = None


@dataclass(slots=True)
class TLSConfig:
    allowInsecure: Optional[bool] = None
    certificates: Optional[list[TLSCertConfig]] = field(
        default_factory=list[TLSCertConfig]
    )
    serverName: Optional[str] = None
    alpn: Optional[list[str]] = field(default_factory=list[str])
    enableSessionResumption: Optional[bool] = None
    disableSystemRoot: Optional[bool] = None
    minVersion: Optional[str] = None
    maxVersion: Optional[str] = None
    cipherSuites: Optional[str] = None
    fingerprint: Optional[str] = None
    rejectUnknownSni: Optional[bool] = None
    pinnedPeerCertificateChainSha256: Optional[list[str]] = field(
        default_factory=list[str]
    )
    pinnedPeerCertificatePublicKeySha256: Optional[list[str]] = field(
        default_factory=list[str]
    )
    masterKeyLog: Optional[str] = None


@dataclass(slots=True)
class REALITYConfig:
    show: Optional[bool] = None
    masterKeyLog: Optional[str] = None
    dest: Optional[dict] = field(default_factory=dict)
    type: Optional[str] = None
    xver: Optional[int] = None
    serverNames: Optional[list[str]] = field(default_factory=list[str])
    privateKey: Optional[str] = None
    minClientVer: Optional[str] = None
    maxClientVer: Optional[str] = None
    maxTimeDiff: Optional[int] = None
    shortIds: Optional[list[str]] = field(default_factory=list[str])
    fingerprint: Optional[str] = None
    serverName: Optional[str] = None
    publicKey: Optional[str] = None
    shortId: Optional[str] = None
    spiderX: Optional[str] = None


@dataclass(slots=True)
class CustomSockoptConfig:
    level: Optional[str] = None
    opt: Optional[str] = None
    value: Optional[str] = None
    type: Optional[str] = None


@dataclass(slots=True)
class SocketConfig:
    mark: Optional[int] = None
    tcpFastOpen: Optional[dict] = field(default_factory=dict)
    tproxy: Optional[str] = None
    acceptProxyProtocol: Optional[bool] = None
    domainStrategy: Optional[str] = None
    dialerProxy: Optional[str] = None
    tcpKeepAliveInterval: Optional[int] = None
    tcpKeepAliveIdle: Optional[int] = None
    tcpCongestion: Optional[str] = None
    tcpWindowClamp: Optional[int] = None
    tcpMaxSeg: Optional[int] = None
    tcpNoDelay: Optional[bool] = None
    tcpUserTimeout: Optional[int] = None
    v6only: Optional[bool] = None
    interface: Optional[str] = None
    tcpMptcp: Optional[bool] = None
    customSockopt: Optional[list[CustomSockoptConfig]] = field(
        default_factory=list[CustomSockoptConfig]
    )


@dataclass(slots=True)
class StreamConfig:
    network: Optional[str] = None
    security: Optional[str] = None
    tlsSettings: Optional[TLSConfig] = field(default_factory=TLSConfig)
    realitySettings: Optional[REALITYConfig] = field(default_factory=REALITYConfig)
    tcpSettings: Optional[TCPConfig] = field(default_factory=TCPConfig)
    kcpSettings: Optional[KCPConfig] = field(default_factory=KCPConfig)
    wsSettings: Optional[WebSocketConfig] = field(default_factory=WebSocketConfig)
    httpSettings: Optional[HTTPConfig] = field(default_factory=HTTPConfig)
    dsSettings: Optional[DomainSocketConfig] = field(default_factory=DomainSocketConfig)
    quicSettings: Optional[QUICConfig] = field(default_factory=QUICConfig)
    sockopt: Optional[SocketConfig] = field(default_factory=SocketConfig)
    grpcSettings: Optional[GRPCConfig] = field(default_factory=GRPCConfig)
    gunSettings: Optional[GRPCConfig] = field(default_factory=GRPCConfig)
    httpupgradeSettings: Optional[HttpUpgradeConfig] = field(
        default_factory=HttpUpgradeConfig
    )
    splithttpSettings: Optional[SplitHTTPConfig] = field(
        default_factory=SplitHTTPConfig
    )


@dataclass(slots=True)
class ProxyConfig:
    tag: Optional[str] = None
    transportLayer: Optional[bool] = None
