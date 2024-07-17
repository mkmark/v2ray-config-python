from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.features.dns as dns


@dataclass(slots=True)
class fakeDNSExtraOpts(int):
    pass


@dataclass(slots=True)
class fakeDNSSniffResult:
    domain_name: Optional[str] = None


@dataclass(slots=True)
class ipAddressInRangeOpt:
    address_in_range: Optional[bool] = None


@dataclass(slots=True)
class DNSThenOthersSniffResult:
    domain_name: Optional[str] = None
    protocol_original_name: Optional[str] = None
