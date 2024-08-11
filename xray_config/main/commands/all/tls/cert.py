from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.protocol.tls.cert as cert
# import xray_config.common.task as task
# import xray_config.main.commands.base as base


@dataclass(slots=True)
class stringList(list[str]):
    pass


@dataclass(slots=True)
class jsonCert:
    certificate: Optional[list[str]] = field(default_factory=list[str])
    key: Optional[list[str]] = field(default_factory=list[str])
