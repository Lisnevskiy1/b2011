from box import Box
class ColorBox(Box):
    def __init__(self, width = None, height = None, color = None):
        super().__init__(width, height)
    self.Color = color
def __str__(self):
    return f"{super().__str__()}\n" \
        f"Color: {self.Color}"