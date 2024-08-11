from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.ocsp as ocsp
# import xray_config.common.platform.filesystem as filesystem
# import xray_config.common.protocol.tls.cert as cert
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class Option(Config)):
    pass
