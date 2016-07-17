#Standard Binary Tree data-Sturcture
class BinaryTree():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

#inserts a new tree node and moves the current one down the tree if one is currently there
    def insert_left(self, data):
        if self.left == None:
            self.left = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.left = self.left
            self.left = tree

    def insert_right(self, data):
        if self.right == None:
            self.right = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.right = self.right
            self.right = tree


#the three different ways to transverse the tree
def pre_order(tree):
    if tree:
        print tree.data
        pre_order(tree.get_left)
        pre_order(tree.get_right)


def in_order(tree):
    if tree != None:
        in_order(tree.get_left)
        print tree.data
        in_order(tree.get_right)


def post_order(tree):
    if tree != None:
        post_order(tree.get_left)
        post_order(tree.get_right)
        print tree.data

