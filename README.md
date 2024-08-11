# v2ray-config-python

python dataclass definition of v2ray/xray config with serialization/deserialization, following pep8 compliance

- NOT complete, and will not be complete due to lack motivation for now
- NO docs, the project is a direct dirty translation of the original go types. If you wonder where to look for certain config settings, search/read the go code.
- half automatic half manually generated (much better than manual typing, same hard to maintain in the long term)
- support v2ray v4 and v5, xray
- reveal lots of hidden stuff not recorded in official document...

last generated on 20240705

## usage

### install

```sh
pip install .
```

### deserialize

```py
import v2ray_config
d: dict                       # usually loaded form json config file
cfg = v2ray_config.Cfgv4(**d)
cfg = v2ray_config.Cfgv5(**d)
```

> [!WARNING]  
> Not all parts of the config are deserialized, e.g. settings of protocols, you need to do manual deserialization using coreesponding class. This is how things are implemented by v2ray-core.

### serialize

```py
import v2ray_config
d = cfg.to_dict(clean=True)   # clean all None, empty list, empty dict recursively
```

## how things were generated

```py
python -m gen.main
```

then manually (unfortunately but too difficult to automate atm) fix dozens of errors and add some features

- reorder some of the class definition to ensure correct definition sequence
- replace some of the field definition from dict (interface in golang) to cooresponding class
  - RawFieldRule
  - v2ray_config.app.log.config_pb.Config
  - v2ray_config.app.dns.config_pb.Config
  - v2ray_config.app.router.config_pb.Config
- add to_dict method
