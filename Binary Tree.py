#Standard Binary Tree data-Sturcture
class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#inserts a new tree node and moves the current one down the tree if one is currently there
    def insert_left(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.left = self.left
            self.left = tree

    def insert_right(self, data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.right = self.right
            self.right = tree


#the three different ways to transverse the tree
def pre_order(tree):
    if tree is not None:
        print tree.data
        pre_order(tree.left)
        pre_order(tree.right)


def in_order(tree):
    if tree is not None:
        in_order(tree.left)
        print tree.data
        in_order(tree.right)


def post_order(tree):
    if tree is not None:
        post_order(tree.left)
        post_order(tree.right)
        print tree.data

