# %%
import glob
import os
from pathlib import Path
import re

from gen.type import go2py

projects = {
    "v2ray-core": {
        "go_base_path": "lib/v2ray-core",
        "out_dir": "out/v2ray_config",
        "base_dir": "v2ray_config",
        "import_pattern": re.compile(r"\"github\.com\/v2fly\/v2ray-core\/v5\/([^\"]*)\""),
    },
    "xray-core": {
        "go_base_path": "lib/xray-core",
        "out_dir": "out/xray_config",
        "base_dir": "xray_config",
        "import_pattern": re.compile(r"\"github\.com\/xtls\/xray-core\/([^\"]*)\""),
    },
}

for project in projects.values():
    go_base_path = project["go_base_path"]
    go_rel_files = glob.glob("**/*.go", recursive=True, root_dir=go_base_path)
    project["go_rel_files"] = go_rel_files

def get_go_file(project, go_rel_file):
    go_base_path = project["go_base_path"]
    return f"{go_base_path}/{go_rel_file}"

def get_py_file(project, go_rel_file: str):
    out_dir = project["out_dir"]
    return f"{out_dir}/{str(Path(go_rel_file).with_suffix("")).replace('.', "_")}.py"

def get_go_path(project, py_path: Path):
    out_dir = project["out_dir"]
    go_base_path = project["go_base_path"]
    return Path(str(py_path).replace(out_dir, go_base_path))

# %%

import shutil

for project in projects.values():
    shutil.rmtree(project["out_dir"], ignore_errors=True)
    os.makedirs(project["out_dir"])

def recursive_init(project, py_path: Path):
    if not os.path.exists(py_path):
        if not os.path.exists(py_path.parent):
            recursive_init(project, py_path.parent)
        
        os.makedirs(py_path)
        with open(f"{py_path}/__init__.py", 'w') as f:
            local_files = glob.glob("*", recursive=False, root_dir=get_go_path(project, py_path))
            for local_file in local_files:
                if "errors.generated" in str(local_file):
                    continue
                if "test" in local_file:
                    continue
                f.write(f"from . import {str(Path(local_file).with_suffix("")).replace('.', "_")}\n")


for project in projects.values():
    for go_rel_file in project["go_rel_files"]:
        go_file = Path(get_go_file(project, go_rel_file))
        if "errors.generated" in str(go_file):
            continue
        if "test" in str(go_file):
            continue

        py_file = Path(get_py_file(project, go_rel_file))
        recursive_init(project, py_file.parent)

        with open(go_file) as f:
            go_txt = f.read()

        py_txt = go2py(project, go_txt)

        with open(get_py_file(project, go_rel_file), 'w') as f:
            f.writelines(py_txt)



# %% danger!
for project in projects.values():
    base_dir = project["base_dir"]
    out_dir = project["out_dir"]
    shutil.rmtree(base_dir, ignore_errors=True)
    shutil.copytree(out_dir, base_dir)
