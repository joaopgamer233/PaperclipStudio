from PyQt5.QtCore import QSize


class Settings:
    APP_NAME = "Paperclip Studio"
    VERSION = "0.1.0"

    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    CANVAS_WIDTH = 1920
    CANVAS_HEIGHT = 1080

    DEFAULT_BRUSH_SIZE = 10
    DEFAULT_BRUSH_COLOR = "#000000"

    AUTOSAVE_INTERVAL = 300000  # 5 minutes

    ICON_SIZE = QSize(24, 24)