from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.browserforwarder as browserforwarder


@dataclass(slots=True)
class BrowserForwarderConfig:
    listen_addr: Optional[str] = None
    listen_port: Optional[int] = None
