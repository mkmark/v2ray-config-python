from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.transport.internet.stat as stat


@dataclass(slots=True)
class ConnHandler(Connection)):
    pass


@dataclass(slots=True)
class ListenFunc(Port, settings *MemoryStreamConfig, handler ConnHandler) (Listener, error)):
    pass
