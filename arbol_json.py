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
    def insert(self, parent: Any, value: Dict, current=None) -> None:
        if self.root is None:
            if parent is None:
                self.root = GeneralNode(value)
                return
            else:
                return

        if current is None:
            current = self.root

        for clave, valor in current.value.items():
            if valor == parent:
                current.children[valor] = GeneralNode(value)
                return

        for child in current.children.values():
            self.insert(parent, value, child)


    def _find(self) -> Optional[GeneralNode]:
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

    def _build_tree_repr(self, node, prefix, is_last):

        tree_str = prefix + ("└── " if is_last else "├── ")
        tree_str += str(node.value["nombre"]) + "\n"

        prefix += "    " if is_last else "│   "

        children = list(node.children.values())

        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)

            tree_str += self._build_tree_repr(
                child,
                prefix,
                is_last_child
            )

        return tree_str

tree = GeneralTree()

# raíz
tree.insert(None, {
    "nombre": "A"
})

# hijos
tree.insert("nombre", {
    "nombre": "B"
})

tree.insert("A", {
    "nombre": "C"
})

# subhijos
tree.insert("B", {
    "nombre": "D"
})



print(tree)