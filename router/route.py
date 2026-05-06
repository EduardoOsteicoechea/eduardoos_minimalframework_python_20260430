from dataclasses import dataclass
from typing import Callable, Coroutine, Any, Union

HandlerType = Union[
    Callable[[Any], Any],
    Callable[[Any], Coroutine[Any,Any,Any]]
]


@dataclass
class Route:
    path: str
    methods: list[str]
    handler: HandlerType
    should_authenticate: bool = False