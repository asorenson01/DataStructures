from tnode import Tnode

class Binarytree:
    def __init__(self):
        self.root = None

    def add_to_tree(self, data):

        if self.root is None:
            self.root = Tnode(data)
            return
        if self.root.data > data:
            if self.root.left is None:
                self.root.left = Tnode(data)
            else:
                x = self.root.left
                if x.data > data:
                    x.left = Tnode(data)



        else:
            if self.root.right is None:
                self.root.right = Tnode(data)
            else:
                pass


        # if self.root.data > data:
        #     self.root.right = Tnode(data)
        # if self.data.data is not None:
        #     if data < self.data:
        #         if self.left is None:
        #             self.left = tnode
        #         else:
        #             self.left.add_to_tree(data)
        # else:
        #     self.data = tnode



