from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class TransferType(int):
    pass


@dataclass(slots=True)
class AddressType(int):
    pass
