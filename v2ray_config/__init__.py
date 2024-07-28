from pydantic import RootModel

from . import app
from . import infra
from . import proxy
from . import transport
from . import common


def remove_empty_elements(d) -> dict:
    """
    recursively remove empty lists, empty dicts, or None elements from a dictionary
    """

    def empty(x):
        return x is None or x == {} or x == [] or x == ""

    if not isinstance(d, (dict, list)):
        return d
    elif isinstance(d, list):
        return [v for v in (remove_empty_elements(v) for v in d) if not empty(v)]
    else:
        return {
            k: v
            for k, v in ((k, remove_empty_elements(v)) for k, v in d.items())
            if not empty(v)
        }


class Cfgv4(infra.conf.v4.v2ray.Config):
    def to_dict(self, clean=True):
        d = RootModel[infra.conf.v4.v2ray.Config](self).model_dump()
        if clean:
            d = remove_empty_elements(d)
        return d


class Cfgv5(infra.conf.v5cfg.skeleton.RootConfig):
    def to_dict(self, clean=True):
        d = RootModel[infra.conf.v5cfg.skeleton.RootConfig](self).model_dump()
        if clean:
            d = remove_empty_elements(d)
        return d
