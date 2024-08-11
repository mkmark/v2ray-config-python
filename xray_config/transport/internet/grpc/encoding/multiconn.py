from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.net.cnc as cnc
# import xray_config.common.signal.done as done


@dataclass(slots=True)
class MultiHunkReaderWriter:
    hc: Optional[MultiHunkConn] = field(default_factory=MultiHunkConn)
    cancel: Optional[CancelFunc] = field(default_factory=CancelFunc)
    done: Optional[Instance] = field(default_factory=Instance)
    buf: Optional[list[list[int]]] = field(default_factory=list[list[int]])
