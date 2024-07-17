from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf


@dataclass(slots=True)
class PlainChunkSizeParser:
    pass


@dataclass(slots=True)
class AEADChunkSizeParser:
    auth: Optional[AEADAuthenticator] = field(default_factory=AEADAuthenticator)


@dataclass(slots=True)
class ChunkStreamReader:
    size_decoder: Optional[ChunkSizeDecoder] = field(default_factory=ChunkSizeDecoder)
    reader: Optional[BufferedReader] = field(default_factory=BufferedReader)
    buffer: Optional[list[int]] = field(default_factory=list[int])
    left_over_size: Optional[int] = None
    max_num_chunk: Optional[int] = None
    num_chunk: Optional[int] = None


@dataclass(slots=True)
class ChunkStreamWriter:
    size_encoder: Optional[ChunkSizeEncoder] = field(default_factory=ChunkSizeEncoder)
    writer: Optional[Writer] = field(default_factory=Writer)
