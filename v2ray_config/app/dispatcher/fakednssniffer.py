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
    domainName: Optional[str] = None


@dataclass(slots=True)
class ipAddressInRangeOpt:
    addressInRange: Optional[bool] = None


@dataclass(slots=True)
class DNSThenOthersSniffResult:
    domainName: Optional[str] = None
    protocolOriginalName: Optional[str] = None
