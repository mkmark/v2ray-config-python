from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Header:
    name: Optional[str] = None
    value: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class Version:
    value: Optional[str] = None


@dataclass(slots=True)
class Method:
    value: Optional[str] = None


@dataclass(slots=True)
class RequestConfig:
    version: Optional[Version] = field(default_factory=Version)
    method: Optional[Method] = field(default_factory=Method)
    uri: Optional[list[str]] = field(default_factory=list[str])
    header: Optional[list[Header]] = field(default_factory=list[Header])


@dataclass(slots=True)
class Status:
    code: Optional[str] = None
    reason: Optional[str] = None


@dataclass(slots=True)
class ResponseConfig:
    version: Optional[Version] = field(default_factory=Version)
    status: Optional[Status] = field(default_factory=Status)
    header: Optional[list[Header]] = field(default_factory=list[Header])


@dataclass(slots=True)
class Config:
    request: Optional[RequestConfig] = field(default_factory=RequestConfig)
    response: Optional[ResponseConfig] = field(default_factory=ResponseConfig)


@dataclass(slots=True)
class x:
    pass
