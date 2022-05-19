from typing import Callable, Set, List
from hashlib import sha1

class Event:
    def __init__(self) -> "Event":
        self.__hash_delegates: Set[str] = set()
        self.__delegates: List[Callable] = []

    def __iadd__(self, delegate: Callable):
        hsha1 = sha1(str(delegate).encode("utf-8")).hexdigest()
        if hsha1 not in self.__hash_delegates:
            self.__hash_delegates.add(hsha1)
            self.__delegates.append(delegate)
        return self

    def __isub__(self, delegate: Callable):
        hsha1 = sha1(str(delegate).encode("utf-8")).hexdigest()
        if hsha1 in self.__hash_delegates:
            self.__hash_delegates.remove(hsha1)
            self.__delegates.remove(delegate)
        return self

    def __call__(self, *args, **kwargs):
        for delegate in self.__delegates:
            delegate(*args, **kwargs)
