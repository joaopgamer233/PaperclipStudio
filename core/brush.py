from PyQt5.QtGui import QColor


class Brush:
    def __init__(self):
        self.size = 10
        self.color = QColor(0, 0, 0)

        self.opacity = 255
        self.hardness = 100

        self.antialias = True

    def set_size(self, size):
        self.size = max(1, int(size))

    def set_color(self, color):
        self.color = QColor(color)

    def set_opacity(self, opacity):
        self.opacity = max(0, min(255, opacity))