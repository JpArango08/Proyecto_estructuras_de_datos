from typing import List, Dict, Any


from typing import Any
class Node:
  def __init__(self, value: Any , next = None):
    self.value = value
    self.next = next

  def __repr__(self) -> str:
     return f"{self.value}"


class LinkedList:
  def __init__(self, head = None):
    self.head = head
    self.size: int = 0

  def delete_at_pos(self, pos: int) -> None:
    if(self.head is None):
      return

    if(pos > 0 and pos >= self.size):
      return

    if(pos == 0):
      old_head_next = self.head.next
      self.head.next = None
      self.head = old_head_next
    else:
      current = self.head
      for i in range(pos - 1):
        current = current.next

      old_current_next_next = current.next.next
      current.next.next = None
      current.next = old_current_next_next

    self.size -= 1

  def append(self, value: Any) -> None:
    if(self.head is None):
      self.head = Node(value) 
    else:
      current_node = self.head
      while(current_node.next is not None):
        current_node = current_node.next

      current_node.next = Node(value)
      
    self.size += 1

  def __len__(self) -> int:
    return self.size

  def traverse(self) -> None:

    current_node = self.head
    while(current_node is not None):
      print(current_node.value)
      current_node = current_node.next

  def __repr__(self) -> str:

      if self.head is None:
          return "[]"

      texto = ""

      current = self.head

      while current is not None:

          texto += str(current.value)

          if current.next is not None:
              texto += " -> "

          current = current.next

      return f"[{texto}]"