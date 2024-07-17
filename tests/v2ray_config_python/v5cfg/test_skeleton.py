# %%
## some below are marked as dict in v5 config, since in go they are implemented as interface
## replace manually for auto generation
from v2ray_config.infra.conf.v5cfg.skeleton import RootConfig
from v2ray_config.infra.conf.synthetic.dns.dns import DNSConfig
from v2ray_config.infra.conf.synthetic.log.log import LogConfig
from v2ray_config.infra.conf.synthetic.router.router import RouterConfig

config = RootConfig()
config
# %%
config.log = LogConfig()
config.dns = DNSConfig()
config.router = RouterConfig()

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
