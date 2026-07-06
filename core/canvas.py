from PyQt5.QtGui import QImage, QColor
from PyQt5.QtCore import Qt

from core.settings import Settings


class Canvas:
    def __init__(self):
        self.image = QImage(
            Settings.CANVAS_WIDTH,
            Settings.CANVAS_HEIGHT,
            QImage.Format_ARGB32
        )

        self.clear()

    def clear(self):
        self.image.fill(Qt.white)

    def width(self):
        return self.image.width()

    def height(self):
        return self.image.height()

    def qimage(self):
        return self.image