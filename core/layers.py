class Layer:
    def __init__(self, name="Layer"):
        self.name = name

        self.visible = True
        self.opacity = 100

        self.image = None


class LayerManager:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer=None):
        if layer is None:
            layer = Layer(f"Layer {len(self.layers)+1}")

        self.layers.append(layer)

    def remove_layer(self, index):
        if 0 <= index < len(self.layers):
            self.layers.pop(index)

    def get_layer(self, index):
        if 0 <= index < len(self.layers):
            return self.layers[index]

        return None

    def count(self):
        return len(self.layers)