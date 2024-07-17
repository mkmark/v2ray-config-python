# %%
import glob
import os
from pathlib import Path

from gen.type import go2py

go_base_path = "lib/v2ray-core"

go_rel_files = glob.glob("**/*.go", recursive=True, root_dir=go_base_path)
go_rel_files

def get_go_file(go_rel_file):
    return f"{go_base_path}/{go_rel_file}"

out_dir = "out/v2ray_config"

def get_py_file(go_rel_file: str):
    return f"{out_dir}/{str(Path(go_rel_file).with_suffix("")).replace('.', "_")}.py"

def get_go_path(py_path: Path):
    return Path(str(py_path).replace(out_dir, go_base_path))

# %%

import shutil

shutil.rmtree(out_dir, ignore_errors=True)
os.makedirs(out_dir)

def recursive_init(py_path: Path):
    if not os.path.exists(py_path):
        if not os.path.exists(py_path.parent):
            recursive_init(py_path.parent)
        
        os.makedirs(py_path)
        with open(f"{py_path}/__init__.py", 'w') as f:
            local_files = glob.glob("*", recursive=False, root_dir=get_go_path(py_path))
            for local_file in local_files:
                if "errors.generated" in str(local_file):
                    continue
                if "test" in local_file:
                    continue
                f.write(f"from . import {str(Path(local_file).with_suffix("")).replace('.', "_")}\n")


for go_rel_file in go_rel_files:
    go_file = Path(get_go_file(go_rel_file))
    if "errors.generated" in str(go_file):
        continue
    if "test" in str(go_file):
        continue

    py_file = Path(get_py_file(go_rel_file))
    recursive_init(py_file.parent)

    with open(go_file) as f:
        go_txt = f.read()

    py_txt = go2py(go_txt)

    with open(get_py_file(go_rel_file), 'w') as f:
        f.writelines(py_txt)



# %% danger!
base_dir = "v2ray_config"
shutil.rmtree(base_dir, ignore_errors=True)
shutil.copytree(out_dir, base_dir)
