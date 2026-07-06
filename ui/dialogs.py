from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Dialogs:

    @staticmethod
    def open_file(parent):
        filename, _ = QFileDialog.getOpenFileName(
            parent,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        return filename

    @staticmethod
    def save_file(parent):
        filename, _ = QFileDialog.getSaveFileName(
            parent,
            "Save Image",
            "",
            "PNG Image (*.png);;JPEG Image (*.jpg)"
        )
        return filename

    @staticmethod
    def info(parent, title, message):
        QMessageBox.information(parent, title, message)

    @staticmethod
    def warning(parent, title, message):
        QMessageBox.warning(parent, title, message)