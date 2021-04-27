from tnode import Tnode


class Binarytree:
    def __init__(self):
        self.root = None

    def add_to_tree(self, data):

        if self.root is None:
            self.root = Tnode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Tnode(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Tnode(data)
            else:
                self._insert(data, cur_node.right)

    def search(self, data):
        if self.root is not None:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right is not None:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left is not None:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

    def in_order(self, root):
        res = []
        if root is not None:
            res = self.in_order(root.left)
            res.append(root.data)
            res = res + self.in_order(root.right)
        return res

    def pre_order(self, root):
        res = []
        if root is not None:
            res.append(root.data)
            res = res + self.pre_order(root.left)
            res = res + self.pre_order(root.right)
        return res
