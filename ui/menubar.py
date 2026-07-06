from PyQt5.QtWidgets import QMenuBar


class MenuBar(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        file_menu = self.addMenu("File")
        edit_menu = self.addMenu("Edit")
        view_menu = self.addMenu("View")
        image_menu = self.addMenu("Image")
        help_menu = self.addMenu("Help")