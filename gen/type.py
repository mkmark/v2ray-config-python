# %%
import re
from pydantic.alias_generators import to_snake


def extract_go_struct_types(go_code) -> list[tuple[str, str]]:
    type_pattern = re.compile(r"\n\s*type\s(\w+)\sstruct\s*")
    pos_list = [
        (m.start(0), m.end(0), m.start(1), m.end(1))
        for m in type_pattern.finditer(go_code)
    ]
    types = []
    for pos in pos_list:
        types.append(
            (
                go_code[pos[2] : pos[3]],
                go_code[pos[1] + 1 : get_ending_brace_pos(go_code, pos[1])],
            )
        )
    return types


def get_ending_brace_pos(go_code, i):
    n = len(go_code)
    lvl = 0
    for idx in range(i, n):
        c = go_code[idx]
        if c == "}":
            lvl -= 1
        elif c == "{":
            lvl += 1
        if lvl == 0:
            break

    return idx - 1


def extract_go_simple_types(go_code) -> list[tuple[str, str]]:
    type_pattern = re.compile(r"\n\s*type\s+(\w+)\s+(.+)")
    types = type_pattern.findall(go_code)
    res = []
    for t in types:
        if "struct" not in t[1] and "interface" not in t[1]:
            res.append(t)
    return res


# Function to extract Go type definitions
def extract_go_imports(go_code) -> list[str]:
    import_pattern = re.compile(r"\"github\.com\/v2fly\/v2ray-core\/v5\/([^\"]*)\"")
    imports = import_pattern.findall(go_code)
    return imports


class Go2py:
    def __init__(self) -> None:
        self.import_lines: list[str] = []


go_field_name_to_ignore = [
    "ctxcfg",
    "cfgctx",
    "state",
    "sizeCache",
    "unknownFields",
]


# Function to convert Go types to Python classes using dataclass
def go2py(go_code: str):
    go_imports = extract_go_imports(go_code)
    go_simple_types = extract_go_simple_types(go_code)
    go_struct_types = extract_go_struct_types(go_code)

    py_file_lines = []
    py_file_lines = [
        "from pydantic.dataclasses import dataclass, Field as field\n",
        "from typing import Optional\n",
    ]

    py_import_lines = []
    for go_import in go_imports:
        py_import = go_import.replace(".", "_").replace("/", ".")
        py_import_split = py_import.split(".")
        if len(py_import_split) < 1:
            continue
        # py_import_from = ".".join(py_import_split[:-1])
        # if py_import_from:
        #     py_import_from = "." + py_import_from
        py_import_as = py_import_split[-1]
        py_import_lines.append(f"# import v2ray_config.{py_import} as {py_import_as}\n")

    if len(py_import_lines):
        py_file_lines.append("\n")
        py_file_lines.extend(py_import_lines)

    for type_name, base_class in go_simple_types:
        py_before_class_lines = [
            "\n",
            "\n",
            "@dataclass(slots=True)\n",
        ]
        py_base_class = go2py_field_type(base_class)
        py_base_classes_str = f"({py_base_class})"
        name_line = f"class {type_name}{py_base_classes_str}:\n"
        class_lines = []
        class_lines.extend(py_before_class_lines)
        class_lines.append(name_line)
        class_lines.append("    pass\n")
        py_file_lines.extend(class_lines)

    for type_name, fields in go_struct_types:
        py_before_class_lines = [
            "\n",
            "\n",
            "@dataclass(slots=True)\n",
        ]
        go_field_lines = fields.strip().split("\n")
        py_base_classes: list[str] = []
        py_field_lines: list[str] = []
        for go_field_line in go_field_lines:
            go_field_line = go_field_line.strip()
            if not go_field_line:
                continue
            if go_field_line.startswith("//"):
                continue
            if " func(" in go_field_line:
                continue

            go_field_elements = go_field_line.split()
            go_field_name = None
            len_go_field_elements = len(go_field_elements)

            if len_go_field_elements == 0:
                continue
            elif len_go_field_elements == 1:
                go_field_name = None
                py_base_classes.append(go2py_field_type(go_field_elements[0]))
            elif len_go_field_elements == 2:
                go_field_name = go_field_elements[0]
            else:
                found = False
                for i in range(2, len_go_field_elements):
                    if go_field_elements[i].startswith("`json:"):
                        found = True
                        go_field_name = go_field_elements[i][7:-2].split(",")[0]
                        break
                if not found:
                    go_field_name = go_field_elements[0]

            if go_field_name in go_field_name_to_ignore:
                continue

            if go_field_name is not None:
                py_field_name = to_snake(go_field_name)
                py_field_name = escape_python_preserved_keyword(py_field_name)
                go_field_type = go_field_elements[1]
                py_field_type = go2py_field_type(go_field_type)
                py_field_lines.append(
                    f"    {py_field_name}: Optional[{py_field_type}] = {get_default_val(py_field_type)}\n"
                )

        if len(py_base_classes):
            py_base_classes_str = f"({", ".join(py_base_classes)})"
        else:
            py_base_classes_str = ""
        name_line = f"class {type_name}{py_base_classes_str}:\n"
        class_lines = []
        class_lines.extend(py_before_class_lines)
        class_lines.append(name_line)
        if len(py_field_lines):
            class_lines.extend(py_field_lines)
        else:
            class_lines.append("    pass\n")

        py_file_lines.extend(class_lines)
    return py_file_lines


def escape_python_preserved_keyword(s):
    if s in ["pass", "from"]:
        return s + "_"
    return s


# Function to convert Go types to Python types
def go2py_field_type(go_field_type: str):
    if go_field_type.startswith("[]"):
        return f"list[{go2py_field_type(go_field_type[2:])}]"
    if go_field_type.startswith("*"):
        return go2py_field_type(go_field_type[1:])
    if go_field_type.startswith("map["):
        res = go_field_type[4:]
        res_split = res.split("]")
        t1 = "]".join(res_split[:-1])
        t2 = res_split[-1]
        return f"dict[{go2py_field_type(t1)}, {go2py_field_type(t2)}]"

    if "." in go_field_type:
        go_field_type = go_field_type.split(".")[-1]

    type_mapping = {
        "string": "str",
        "int": "int",
        "interface{}": "dict",
        "byte": "int",
        "int16": "int",
        "int32": "int",
        "int64": "int",
        "uint8": "int",
        "uint16": "int",
        "uint32": "int",
        "uint64": "int",
        "float32": "float",
        "float64": "float",
        #
        "RawMessage": "dict",
        "json.RawMessage": "dict",
        "net.Address": "str",
        "Address": "str",
        "Duration": "str",
        "duration.Duration": "str",
        "StringList": "list[str]",
        "Address": "str",
        "Network": "str",
        "PortRange": "str",
        "PortList": "list[str]",
        "NetworkList": "list[str]",
        "cfgcommon.StringList": "list[str]",
        "cfgcommon.Address": "str",
        "cfgcommon.Network": "str",
        "cfgcommon.PortRange": "str",
        "cfgcommon.PortList": "list[str]",
        "cfgcommon.NetworkList": "list[str]",
        "Port": "int",
        "net.Port": "int",
    }
    py_field_type = type_mapping.get(go_field_type, go_field_type)
    return py_field_type


def get_default_val(py_field: str) -> str:
    if py_field in ["str", "int", "float", "bool"]:
        return None
    return f"field(default_factory={py_field})"


if __name__ == "__main__":
    # Sample Go code
    go_code = """
package main

import (
    "github.com/v2fly/v2ray-core/v5/common/serial"
)

type ServerConfig struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Users          []*protocol.User          `protobuf:"bytes,1,rep,name=users,proto3" json:"users,omitempty"`
	Fallbacks      []*Fallback               `protobuf:"bytes,3,rep,name=fallbacks,proto3" json:"fallbacks,omitempty"`
	PacketEncoding packetaddr.PacketAddrType `protobuf:"varint,4,opt,name=packet_encoding,json=packetEncoding,proto3,enum=v2ray.core.net.packetaddr.PacketAddrType" json:"packet_encoding,omitempty"`
}


    type Company struct {
        Name        string
        Employees   []Person
        FoundedYear int
    }

type DeterministicDice struct {
	*rand.Rand
}

"""

    # Extract Go type definitions
    go_types = go2py(go_code)

    print("".join(go_types))

    # %%
