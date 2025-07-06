from dataclasses import dataclass

@dataclass
class Sprite:
    name: str
    pos: tuple[int, int]
    size: tuple[int, int]