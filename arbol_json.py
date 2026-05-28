from typing import Any, Optional, Dict
from lista_enlazada import LinkedList
class GeneralNode:
    def __init__(self, value: Dict):
        self.value = value
        self.children: LinkedList = LinkedList()

    def __repr__(self):
        if len(self.children) == 0:
            # hoja: mostrar clave: valor
            items = list(self.value.items())
            if items:
                clave, valor = items[0]
                return f"{clave}: {valor!r}"
        # nodo intermedio: mostrar solo la clave
        return list(self.value.keys())[0]

class GeneralTree:
    def __init__(self):
        self.root: Optional[GeneralNode] = None

    def insert(self, parent: Any, value: Dict) -> None:

        new_node = GeneralNode(value)

        if self.root is None:
            if parent is None:
                self.root = new_node
            else:
                print(f"⚠️ Árbol vacío. No existe el padre '{parent}'.")
            return

        parent_node = self._find(self.root, parent)
        if parent_node:
            parent_node.children.append(new_node)
        else:
            print(f"⚠️ No se encontró el nodo padre con valor '{parent}'.")



    def _find(self, node: GeneralNode, value: Any) -> Optional[GeneralNode]:

        if node is None:
            return None

        for clave in node.value.keys():

            if clave == value:
                return node

        current = node.children.head

        while current is not None:

            found = self._find(current.value,value)
            
            if found is not None:
                return found

            current = current.next

        return None

    def __repr__(self) -> str:
        
        if not self.root:
            return "🌱 Árbol vacío"
        return self._build_tree_repr(self.root, "", True)

    def _build_tree_repr(self,node: GeneralNode,prefix: str,is_last: bool) -> str:

        connector = "└── " if is_last else "├── "

        tree_str = prefix + connector + repr(node) + "\n"

        prefix += "    " if is_last else "│   "

        current = node.children.head

        while current is not None:

            siguiente = current.next

            child_is_last = siguiente is None

            tree_str += self._build_tree_repr(
                current.value,
                prefix,
                child_is_last
            )

            current = current.next

        return tree_str