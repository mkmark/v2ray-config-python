from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class V2JsonProtobufListFollower(List):
    pass
