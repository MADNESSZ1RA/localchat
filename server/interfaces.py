from typing import Protocol

class IChatServer(Protocol):
    def run(self) -> None: ...
