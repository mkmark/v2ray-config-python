from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.infra.conf.geodata as geodata


@dataclass(slots=True)
class configureLoadingContext(int):
    pass


@dataclass(slots=True)
class configureLoadingEnvironment:
    geo_loader: Optional[Loader] = field(default_factory=Loader)
