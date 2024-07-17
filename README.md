# v2ray-config-python

python dataclass definition of v2ray config with serialization/deserialzation, following pep8 compliance

- automatic (but dirty) generated
- support both v4 and v5
- reveal lots of hidden stuff not recorded in official document...

last generated on 20240705

## usage

### deserialize

```py
import v2ray_config
d: dict                       # usually loaded form json config file
cfg = v2ray_config.Cfgv4(**d)
cfg = v2ray_config.Cfgv5(**d)
```

> [!WARNING]  
> Not all part of the config is deserialized, e.g. settings of protocols, you need to do manual deserialization using coreesponding class

### serialize

```py
import v2ray_config
d = cfg.to_dict(clean=True)              # clean all None, empty list, empty dict recursively
```

## generate

```py
python -m gen.main
```

then manually (unfortunately but to difficult to automate atm) fix dozens of errors and add some features

- reorder some of the class definition to ensure correct definition sequence
- replace some of the field definition from dict (interface in golang) to cooresponding class
  - RawFieldRule
  - DNSConfig
  - LogConfig
  - RouterConfig
- add to_dict method
