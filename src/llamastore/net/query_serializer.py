from typing import Any, Dict, List
from enum import Enum

explode = bool


def simple(value: Any, explode: bool) -> str:
    if isinstance(value, Enum):
        return str(value.value)

    # Check if the value is a list
    if isinstance(value, list):
        return ",".join(value) if explode else "".join(value)

    if isinstance(value, dict):
        if explode:
            # Serialize object with exploded format: "key=value,key2=value2"
            return ",".join([f"{k}={v}" for k, v in value.items()])
        else:
            # Serialize object with non-exploded format: "key,value,key2,value2"
            return ",".join(
                [str(item) for sublist in value.items() for item in sublist]
            )

    return str(value)


style_methods = {
    "simple": simple,
}


def serialize_path(
    parameter_style, explode: bool, parameter_value: Any, parameter_key=None
):
    method = style_methods.get(parameter_style)
    if not method:
        return ""

    # The `simple` and `label` styles do not require a `parameter_key`
    if not parameter_key:
        return method(parameter_value, explode)
    else:
        return method(parameter_key, parameter_value, explode)
