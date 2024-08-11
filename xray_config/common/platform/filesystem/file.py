from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.platform as platform


@dataclass(slots=True)
class FileReaderFunc(ReadCloser, error)):
    pass
