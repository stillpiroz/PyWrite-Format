class Registry:
    def __init__(self):
        self._nodes = {}

    def register(self, name, node_class):
        if name in self._nodes:
            raise ValueError(f"Node '{name}' is already registered.")

        self._nodes[name] = node_class

    def get(self, name):
        try:
            return self._nodes[name]
        except KeyError:
            raise ValueError(f"Unknown node type: '{name}'.") from None

    def get_name(self, node_class):
        for name, registered_class in self._nodes.items():
            if registered_class is node_class:
                return name

        raise ValueError(
            f"Node class '{node_class.__name__}' is not registered."
        )
