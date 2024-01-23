from typing import Tuple

from .color import Color


class Palette:

    def __init__(self, colors: Tuple[Tuple[int]]):

        self.colors_ = tuple(Color(c[0], c[1], c[2]) for c in colors)

    def __len__(self) -> int:

        return len(self.colors_)

    @property
    def rgb(self) -> Tuple[Tuple[int]]:

        return tuple(c.rgb for c in self.colors_)
    
    @property
    def hex(self) -> Tuple[str]:

        return tuple(c.hex for c in self.colors_)