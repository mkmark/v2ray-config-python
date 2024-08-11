from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf


@dataclass(slots=True)
class PlainChunkSizeParser:
    pass


@dataclass(slots=True)
class AEADChunkSizeParser:
    auth: Optional[AEADAuthenticator] = field(default_factory=AEADAuthenticator)


@dataclass(slots=True)
class ChunkStreamReader:
    sizeDecoder: Optional[ChunkSizeDecoder] = field(default_factory=ChunkSizeDecoder)
    reader: Optional[BufferedReader] = field(default_factory=BufferedReader)
    buffer: Optional[list[int]] = field(default_factory=list[int])
    leftOverSize: Optional[int] = None
    maxNumChunk: Optional[int] = None
    numChunk: Optional[int] = None


@dataclass(slots=True)
class ChunkStreamWriter:
    sizeEncoder: Optional[ChunkSizeEncoder] = field(default_factory=ChunkSizeEncoder)
    writer: Optional[Writer] = field(default_factory=Writer)
