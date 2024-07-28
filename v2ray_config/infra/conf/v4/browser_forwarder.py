from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.browserforwarder as browserforwarder


@dataclass(slots=True)
class BrowserForwarderConfig:
    listenAddr: Optional[str] = None
    listenPort: Optional[int] = None
