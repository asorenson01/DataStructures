from tnode import Tnode

class Binarytree:

    def creat_tree(self, data):
        root = Tnode(data)
        return root

    def add_to_tree(self, data):
        tnode = data
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = tnode
                else:
                    self.left.add_to_tree(data)
        else:
            self.data = tnode



