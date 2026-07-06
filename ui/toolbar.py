from PyQt5.QtWidgets import QToolBar
from PyQt5.QtCore import QSize


class ToolBar(QToolBar):

    def __init__(self):
        super().__init__("Tools")

        self.setIconSize(QSize(24, 24))
        self.setMovable(False)