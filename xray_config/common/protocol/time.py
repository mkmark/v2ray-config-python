from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.dice as dice


@dataclass(slots=True)
class Timestamp(int):
    pass


@dataclass(slots=True)
class TimestampGenerator(func() Timestamp):
    pass
