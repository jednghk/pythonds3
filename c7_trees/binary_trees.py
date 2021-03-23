class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        new_tree = BinaryTree(new_node)
        if self.left_child is None:
            self.left_child = new_tree
        else:
            new_tree.left_child = self.left_child
            self.left_child = new_tree

    def insert_right(self, new_node):
        new_tree = BinaryTree(new_node)
        if self.right_child is None:
            self.right_child = new_tree
        else:
            new_tree.right_child = self.right_child
            self.right_child = new_tree.right_child

    def get_root_val(self):
        return self.key

    def set_root_val(self, new_val):
        self.key = new_val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child


a_tree = BinaryTree("a")
print(a_tree.get_root_val())
print(a_tree.get_left_child())
a_tree.insert_left("b")
print(a_tree.get_left_child())
print(a_tree.get_left_child().get_root_val())
a_tree.insert_right("c")
print(a_tree.get_right_child())
print(a_tree.get_right_child().get_root_val())
a_tree.get_right_child().set_root_val("hello")
print(a_tree.get_right_child().get_root_val())