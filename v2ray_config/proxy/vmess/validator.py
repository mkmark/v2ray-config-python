from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.dice as dice
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial
# import v2ray_config.common.task as task
# import v2ray_config.proxy.vmess.aead as aead


# @dataclass(slots=True)
# class user:
#     user: Optional[MemoryUser] = field(default_factory=MemoryUser)
#     last_sec: Optional[Timestamp] = field(default_factory=Timestamp)


# @dataclass(slots=True)
# class TimedUserValidator(RWMutex):
#     users: Optional[list[user]] = field(default_factory=list[user])
#     user_hash: Optional[dict[[16]byte, indexTimePair]] = field(default_factory=dict[[16]byte, indexTimePair])
#     hasher: Optional[IDHash] = field(default_factory=IDHash)
#     base_time: Optional[Timestamp] = field(default_factory=Timestamp)
#     task: Optional[Periodic] = field(default_factory=Periodic)
#     behavior_seed: Optional[int] = None
#     behavior_fused: Optional[bool] = None
#     aead_decoder_holder: Optional[AuthIDDecoderHolder] = field(default_factory=AuthIDDecoderHolder)
#     legacy_warn_shown: Optional[bool] = None


# @dataclass(slots=True)
# class indexTimePair:
#     user: Optional[user] = field(default_factory=user)
#     time_inc: Optional[int] = None
#     tainted_fuse: Optional[int] = None
