from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.signal.done as done


@dataclass(slots=True)
class DefaultDialerClient:
    transportConfig: Optional[Config] = field(default_factory=Config)
    download: Optional[Client] = field(default_factory=Client)
    upload: Optional[Client] = field(default_factory=Client)
    isH2: Optional[bool] = None
    isH3: Optional[bool] = None
    uploadRawPool: Optional[Pool] = field(default_factory=Pool)
