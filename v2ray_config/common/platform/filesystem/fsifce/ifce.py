from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class FileSeekerFunc(ReadSeekCloser, error)):
    pass


@dataclass(slots=True)
class FileReaderFunc(ReadCloser, error)):
    pass


@dataclass(slots=True)
class FileWriterFunc(WriteCloser, error)):
    pass
