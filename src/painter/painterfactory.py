from .base import BasePainter
from .hardgamepainter import HardGamePainter
from .easygamepainter import EasyGamePainter
from .spacemanpainter import SpacemanPainter

class PainterFactory:
    def get_painter(self, max_fails, variant, mask = " - "):
        if variant == 1:
            if max_fails == 8:
                return BasePainter(mask)
            elif max_fails == 4:
                return HardGamePainter(mask)
            elif max_fails == 12:
                return EasyGamePainter(mask)
        elif variant == 2:
            if max_fails == 8:
                return SpacemanPainter(mask)
