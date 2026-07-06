from core.settings import Settings


class PaperclipStudio:
    def __init__(self):
        self.name = Settings.APP_NAME
        self.version = Settings.VERSION

        self.current_tool = "brush"
        self.current_color = Settings.DEFAULT_BRUSH_COLOR
        self.brush_size = Settings.DEFAULT_BRUSH_SIZE

        self.current_project = None