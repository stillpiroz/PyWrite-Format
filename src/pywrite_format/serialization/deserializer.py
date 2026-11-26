from pywrite_format.nodes.blocks import Paragraph, Image
from pywrite_format.nodes.inlines import Text, Link
from pywrite_format.styles import Alignment


class Deserializer:
    def __init__(self, registry, asset_manager):
        self.registry = registry
        self.asset_manager = asset_manager

    def deserialize(self, data):
        return self._deserialize_node(data)

    def _deserialize_node(self, data):
        node_type = data["type"]
        node_class = self.registry.get(node_type)

        if node_class is Text:
            return Text(data["text"])

        if node_class is Image:
            image_data = self.asset_manager.get(data["asset_path"])
            return Image(image_data)

        if node_class is Link:
            children = [
                self._deserialize_node(child)
                for child in data["children"]
            ]

            return Link(
                url=data["url"],
                children=children
            )

        if node_class is Paragraph:
            children = [
                self._deserialize_node(child)
                for child in data["children"]
            ]

            return Paragraph(
                children=children,
                alignment=Alignment(data["alignment"]),
                indentation=data["indentation"],
                spacing_before=data["spacing_before"],
                spacing_after=data["spacing_after"],
                line_spacing=data["line_spacing"],
            )

        if "children" in data:
            children = [
                self._deserialize_node(child)
                for child in data["children"]
            ]

            return node_class(children)
