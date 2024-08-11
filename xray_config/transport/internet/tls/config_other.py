from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors


@dataclass(slots=True)
class rootCertsCache(Mutex):
    pool: Optional[CertPool] = field(default_factory=CertPool)
