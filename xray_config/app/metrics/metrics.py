from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.observatory as observatory
# import xray_config.app.stats as stats
# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.signal.done as done
# import xray_config.core as core
# import xray_config.features.extension as extension
# import xray_config.features.outbound as outbound
# import xray_config.features.stats as stats


@dataclass(slots=True)
class MetricsHandler:
    ohm: Optional[Manager] = field(default_factory=Manager)
    statsManager: Optional[Manager] = field(default_factory=Manager)
    observatory: Optional[Observatory] = field(default_factory=Observatory)
    tag: Optional[str] = None
