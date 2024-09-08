from typing import Union, List, Dict

JSONSerializable = Union[None, int, str, bool, List["JSONSerializable"], Dict[str, "JSONSerializable"]]