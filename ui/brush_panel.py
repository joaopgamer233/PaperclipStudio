from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt


class BrushPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Brush Size"))

        self.size_slider = QSlider(Qt.Horizontal)
        self.size_slider.setMinimum(1)
        self.size_slider.setMaximum(100)
        self.size_slider.setValue(10)

        layout.addWidget(self.size_slider)