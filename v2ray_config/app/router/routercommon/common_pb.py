from enum import StrEnum
from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Domain_Type(int):
    pass


@dataclass(slots=True)
class Domain:
    type: Optional[str] = None
    value: Optional[str] = None
    # attribute: Optional[list[Domain_Attribute]] = field(
    #     default_factory=list[Domain_Attribute]
    # )


@dataclass(slots=True)
class CIDR:
    ip: Optional[list[int]] = field(default_factory=list[int])
    prefix: Optional[int] = None
    ip_addr: Optional[str] = None


@dataclass(slots=True)
class GeoIP:
    country_code: Optional[str] = None
    cidr: Optional[list[CIDR]] = field(default_factory=list[CIDR])
    inverse_match: Optional[bool] = None
    resource_hash: Optional[list[int]] = field(default_factory=list[int])
    code: Optional[str] = None
    file_path: Optional[str] = None


@dataclass(slots=True)
class GeoIPList:
    entry: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])


@dataclass(slots=True)
class GeoSite:
    country_code: Optional[str] = None
    domain: Optional[list[Domain]] = field(default_factory=list[Domain])
    resource_hash: Optional[list[int]] = field(default_factory=list[int])
    code: Optional[str] = None
    file_path: Optional[str] = None


@dataclass(slots=True)
class GeoSiteList:
    entry: Optional[list[GeoSite]] = field(default_factory=list[GeoSite])


@dataclass(slots=True)
class Domain_Attribute_BoolValue:
    bool_value: Optional[bool] = None


@dataclass(slots=True)
class Domain_Attribute_IntValue:
    int_value: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
