from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.antireplay as antireplay


@dataclass(slots=True)
class AuthIDDecoder:
    s: Optional[Block] = field(default_factory=Block)


@dataclass(slots=True)
class AuthIDDecoderHolder:
    decoders: Optional[dict[str, AuthIDDecoderItem]] = field(default_factory=dict[str, AuthIDDecoderItem])
    filter: Optional[ReplayFilter] = field(default_factory=ReplayFilter)


@dataclass(slots=True)
class AuthIDDecoderItem:
    dec: Optional[AuthIDDecoder] = field(default_factory=AuthIDDecoder)
    ticket: Optional[dict] = field(default_factory=dict)
