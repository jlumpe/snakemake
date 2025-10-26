from typing import FrozenSet, Set, TypeAlias, TypeVar, Union
from os import PathLike


T = TypeVar("T")
AnySet = Union[Set[T], FrozenSet[T]]

#: File system path as string or pathlike object.
StrPath: TypeAlias = str | PathLike
