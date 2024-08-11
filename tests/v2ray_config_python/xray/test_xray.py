# %%
from xray_config.infra.conf.xray import Config

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
