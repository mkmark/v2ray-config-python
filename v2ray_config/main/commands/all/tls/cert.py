from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.protocol.tls.cert as cert
# import v2ray_config.common.task as task
# import v2ray_config.main.commands.base as base


@dataclass(slots=True)
class stringList(list[str]):
    pass


@dataclass(slots=True)
class jsonCert:
    certificate: Optional[list[str]] = field(default_factory=list[str])
    key: Optional[list[str]] = field(default_factory=list[str])
