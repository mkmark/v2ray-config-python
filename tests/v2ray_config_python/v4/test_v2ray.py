# %%
from v2ray_config.infra.conf.v4.v2ray import Config

config = Config()
config
# %%
import dataclasses, json


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


json.dumps(config, cls=EnhancedJSONEncoder)
# %%
assert 1

# %%
