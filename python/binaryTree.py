class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left:Node = None
        self.right:Node = None
        self.parent:Node = None
    def __repr__(self) -> str:
        """Returns a string representation of the node"""
        return f"Node({self.value})"
    def visit(self) -> None:
        if self.left != None:
            self.left.visit()
        print(self.value)
        if self.right != None:
            self.right.visit()
    def search(self,value) -> None:
        if self.value == value:
            print(f"found {value}")
        elif value<self.value and self.left != None:
            self.left.search(value)
        elif value>self.value and self.right != None:
            self.right.search(value)
class Tree:
    def __init__(self) -> None:
        self.root:Node = None

    def insert(self, value: int) -> None:
        """add value to tree"""
        if self.root == None:
            self.root:Node = Node(value)
        else:
            self._insert(value, self.root)
    def _insert(self, value: int, node: Node) -> None:
        """Inserts a value into the tree"""
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
                node.left.parent = node
            else:
                self._insert(value, node.left)
        else:
            if node.right == None:
                node.right = Node(value)
                node.right.parent = node
            else:
                self._insert(value, node.right)
    def traverse(self) -> None:
        """Traverses the tree"""
        self.root.visit()
    def search(self,value) -> None:
        if self.root != None:
            self._search(value,self.root)
    def _search(self,value:int,node:Node) -> None:
        if node.value == value:
            print(f"found {value}")
        elif value<node.value and node.left != None:
            node.left.search(value)
        elif value>node.value and node.right != None:
            node.right.search(value)
    # def __repr__(self) -> str:
    #     """Returns a string representation of the tree"""
    #     """In order traversal"""
    #     result:str = ""
    #     for node in self._in_order(self.root):
    #         result += str(node.value)
    #         result += "-"
    #     return result
def main():
    tree = Tree()
    tree.insert(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(1)

    tree.traverse()
    tree.search(6)
    tree.search(7)
if __name__ == "__main__":
    main()
