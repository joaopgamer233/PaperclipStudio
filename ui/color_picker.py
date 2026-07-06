from PyQt5.QtWidgets import QColorDialog


class ColorPicker:

    @staticmethod
    def pick(parent=None):
        color = QColorDialog.getColor(parent=parent)

        if color.isValid():
            return color

        return None