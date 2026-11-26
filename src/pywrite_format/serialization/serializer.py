from pywrite_format.nodes.blocks import Paragraph, Image
from pywrite_format.nodes.inlines import Text, Link


class Serializer:
    def __init__(self, registry, asset_manager):
        self.registry = registry
        self.asset_manager = asset_manager

    def serialize(self, node):
        return self._serialize_node(node)

    def _serialize_node(self, node):
        node_type = self.registry.get_name(type(node))

        data = {
            "type": node_type
        }

        if isinstance(node, Text):
            data["text"] = node.text

        if hasattr(node, "children"):
            data["children"] = [
                self._serialize_node(child)
                for child in node.children
            ]

        if isinstance(node, Paragraph):
            data["alignment"] = node.alignment.value
            data["indentation"] = node.indentation
            data["spacing_before"] = node.spacing_before
            data["spacing_after"] = node.spacing_after
            data["line_spacing"] = node.line_spacing
        
        if isinstance(node, Link):
            data["url"] = node.url
        
        if isinstance(node, Image):
            data["asset_path"] = self.asset_manager.add(node.image_data)
        
        return data
