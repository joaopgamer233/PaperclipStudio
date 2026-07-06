class Tools:
    BRUSH = "brush"
    ERASER = "eraser"
    EYEDROPPER = "eyedropper"
    FILL = "fill"
    LINE = "line"
    RECTANGLE = "rectangle"
    ELLIPSE = "ellipse"
    TEXT = "text"
    SELECT = "select"
    MOVE = "move"


class ToolManager:
    def __init__(self):
        self.current_tool = Tools.BRUSH

    def set_tool(self, tool):
        self.current_tool = tool

    def get_tool(self):
        return self.current_tool