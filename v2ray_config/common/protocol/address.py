from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class AddressOption(func(*option)):
    pass


@dataclass(slots=True)
class AddressTypeParser(func(byte) byte):
    pass


@dataclass(slots=True)
class option:
    addrTypeMap: Optional[AddressFamily] = field(default_factory=AddressFamily)
    addrByteMap: Optional[[16]byte] = field(default_factory=[16]byte)
    portFirst: Optional[bool] = None
    typeParser: Optional[AddressTypeParser] = field(default_factory=AddressTypeParser)


@dataclass(slots=True)
class portFirstAddressParser:
    ap: Optional[addressParser] = field(default_factory=addressParser)


@dataclass(slots=True)
class portLastAddressParser:
    ap: Optional[addressParser] = field(default_factory=addressParser)


@dataclass(slots=True)
class addressParser:
    addrTypeMap: Optional[AddressFamily] = field(default_factory=AddressFamily)
    addrByteMap: Optional[[16]byte] = field(default_factory=[16]byte)
    typeParser: Optional[AddressTypeParser] = field(default_factory=AddressTypeParser)
