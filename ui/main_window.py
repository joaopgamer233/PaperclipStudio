from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QDockWidget
)
from PyQt5.QtCore import Qt

from ui.toolbar import ToolBar
from ui.menubar import MenuBar
from ui.statusbar import StatusBar
from ui.brush_panel import BrushPanel
from ui.layer_panel import LayerPanel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paperclip Studio")

        self.resize(1280, 720)

        self.setMenuBar(MenuBar(self))
        self.addToolBar(ToolBar())
        self.setStatusBar(StatusBar())

        central = QWidget()
        central_layout = QHBoxLayout(central)
        self.setCentralWidget(central)

        self.brush_panel = BrushPanel()
        self.layer_panel = LayerPanel()

        brush_dock = QDockWidget("Brush", self)
        brush_dock.setWidget(self.brush_panel)
        self.addDockWidget(Qt.LeftDockWidgetArea, brush_dock)

        layer_dock = QDockWidget("Layers", self)
        layer_dock.setWidget(self.layer_panel)
        self.addDockWidget(Qt.RightDockWidgetArea, layer_dock)