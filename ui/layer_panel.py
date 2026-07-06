from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout


class LayerPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.layer_list = QListWidget()

        layout.addWidget(self.layer_list)

    def add_layer(self, name):
        self.layer_list.addItem(name)