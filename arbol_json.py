from typing import Any, Optional, Dict

class GeneralNode:
    def __init__(self, value: Any):
        self.value = value
        self.children: Dict = {}

    def __repr__(self):
        return f"{self.value}"


class GeneralTree:
    def __init__(self):
        self.root: Optional[GeneralNode] = None

    def insert(self, parent: Optional[Any], value: Any, key: str = None) -> None:

        new_node = GeneralNode(value)

        if key is not None:
            node_key = key
        else:
            node_key = str(value)

        if self.root is None:
            if parent is None:
                self.root = new_node
            else:
                print(f"⚠️ Árbol vacío. No existe el padre '{parent}'.")
            return

        parent_node = self._find(self.root, parent)
        if parent_node:
            parent_node.children[node_key] = new_node
        else:
            print(f"⚠️ No se encontró el nodo padre con valor '{parent}'.")

    def _find(self, node: GeneralNode, value: Any) -> Optional[GeneralNode]:
        """Búsqueda DFS del nodo con un valor dado."""
        if node.value == value:
            return node
        for child in node.children.values():
            found = self._find(child, value)
            if found:
                return found
        return None

    def __repr__(self) -> str:
        
        if not self.root:
            return "🌱 Árbol vacío"
        return self._build_tree_repr(self.root, "", True)

    def _build_tree_repr(self, node: GeneralNode, prefix: str, is_last: bool) -> str:

        tree_str = prefix + ("└── " if is_last else "├── ") + str(node.value) + "\n"
        prefix += "    " if is_last else "│   "


        child_count = len(node.children)
        for i, child in enumerate(node.children):
            is_last_child = (i == child_count - 1)
            tree_str += self._build_tree_repr(child, prefix, is_last_child)
        return tree_str