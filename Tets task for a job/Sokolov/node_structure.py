from dataclasses import dataclass


@dataclass
class Node:
    id: int
    name: str
    sort: int
    parent: str
    level: int
