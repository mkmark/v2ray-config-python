from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors


@dataclass(slots=True)
class pfiocNatlook:
    saddr: Optional[[16]byte] = field(default_factory=[16]byte)
    daddr: Optional[[16]byte] = field(default_factory=[16]byte)
    rsaddr: Optional[[16]byte] = field(default_factory=[16]byte)
    rdaddr: Optional[[16]byte] = field(default_factory=[16]byte)
    sport: Optional[int] = None
    dport: Optional[int] = None
    rsport: Optional[int] = None
    rdport: Optional[int] = None
    af: Optional[int] = None
    proto: Optional[int] = None
    direction: Optional[int] = None
    pad: Optional[[1]byte] = field(default_factory=[1]byte)
