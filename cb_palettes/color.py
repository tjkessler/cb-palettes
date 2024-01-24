import colorsys
from typing import Tuple


class Color:

    def __init__(self, r: int, g: int, b: int):

        assert 0 <= r <= 255
        assert 0 <= g <= 255
        assert 0 <= b <= 255

        self.r_ = r
        self.g_ = g
        self.b_ = b

    @property
    def hex(self) -> str:

        return "#%02x%02x%02x" % (self.r_, self.g_, self.b_)
    
    @property
    def hsv(self) -> Tuple[float]:

        return colorsys.rgb_to_hsv(self.r_, self.g_, self.b_)
    
    @property
    def rgb(self) -> Tuple[int]:

        return (self.r_, self.g_, self.b_)
    
    @property
    def rgb_norm(self) -> Tuple[float]:

        return (self.r_ / 255.0, self.g_ / 255.0, self.b_ / 255.0)
