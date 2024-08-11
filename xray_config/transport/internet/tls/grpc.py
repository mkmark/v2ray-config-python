from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class grpcUtlsInfo(CommonAuthInfo):
    state: Optional[ConnectionState] = field(default_factory=ConnectionState)
    sPIFFEID: Optional[URL] = field(default_factory=URL)


@dataclass(slots=True)
class grpcUtls:
    config: Optional[Config] = field(default_factory=Config)
    fingerprint: Optional[ClientHelloID] = field(default_factory=ClientHelloID)
