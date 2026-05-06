from dataclasses import dataclass, field


@dataclass
class HTTPRequest:
    method: str
    path: str
    headers: dict
    body: str
    cookies: dict = field(default_factory=dict)