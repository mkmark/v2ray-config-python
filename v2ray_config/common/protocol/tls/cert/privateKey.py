from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class ecPrivateKey:
    version: Optional[int] = None
    private_key: Optional[list[int]] = field(default_factory=list[int])
    named_curve_oid: Optional[ObjectIdentifier] = field(default_factory=ObjectIdentifier)
    public_key: Optional[BitString] = field(default_factory=BitString)


@dataclass(slots=True)
class pkcs8:
    version: Optional[int] = None
    algo: Optional[AlgorithmIdentifier] = field(default_factory=AlgorithmIdentifier)
    private_key: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class pkcs1AdditionalRSAPrime:
    prime: Optional[Int] = field(default_factory=Int)
    exp: Optional[Int] = field(default_factory=Int)
    coeff: Optional[Int] = field(default_factory=Int)


@dataclass(slots=True)
class pkcs1PrivateKey:
    version: Optional[int] = None
    n: Optional[Int] = field(default_factory=Int)
    e: Optional[int] = None
    d: Optional[Int] = field(default_factory=Int)
    p: Optional[Int] = field(default_factory=Int)
    q: Optional[Int] = field(default_factory=Int)
    dp: Optional[Int] = field(default_factory=Int)
    dq: Optional[Int] = field(default_factory=Int)
    qinv: Optional[Int] = field(default_factory=Int)
    additional_primes: Optional[list[pkcs1AdditionalRSAPrime]] = field(default_factory=list[pkcs1AdditionalRSAPrime])
