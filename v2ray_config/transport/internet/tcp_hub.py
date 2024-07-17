from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net


@dataclass(slots=True)
class ConnHandler(func(Connection)):
    pass


@dataclass(slots=True)
class ListenFunc(Port, settings *MemoryStreamConfig, handler ConnHandler) (Listener, error)):
    pass
