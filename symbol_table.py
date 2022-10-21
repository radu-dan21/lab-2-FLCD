from typing import Optional

from node import Node


class SymbolTable:
    def __init__(self):
        self.__root: Optional[Node] = None

    def insert(self, token: str) -> None:
        node: Node = Node(token)

        if self.__root is None:
            self.__root = node
        else:
            self._insert_recursive(self.__root, node)

    def _insert_recursive(self, current_node: Node, node_to_insert: Node) -> None:
        if node_to_insert < current_node:
            if current_node.left is None:
                current_node.left = node_to_insert
            else:
                self._insert_recursive(current_node.left, node_to_insert)
        elif node_to_insert > current_node:
            if current_node.right is None:
                current_node.right = node_to_insert
            else:
                self._insert_recursive(current_node.right, node_to_insert)

    def contains(self, token: str) -> bool:
        return self._contains_recursive(self.__root, token)

    def _contains_recursive(self, current_node: Node, token: str) -> bool:
        if current_node is None:
            return False
        if current_node.token == token:
            return True

        if token < current_node.token:
            return self._contains_recursive(current_node.left, token)
        return self._contains_recursive(current_node.right, token)
