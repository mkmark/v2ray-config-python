from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.main.commands.base as base
# import xray_config.main.distro.all as all


@dataclass(slots=True)
class null:
    pass
