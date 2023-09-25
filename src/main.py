
# Add a class that will represent the registrar system


from registrar import Registrar
from course import Course
from avl_tree import AVLTree


if __name__ == "__main__":
    tree = AVLTree()
    # Insert some keys into the tree
    tree.root = tree.insert(tree.root, 10)
    tree.root = tree.insert(tree.root, 20)
    tree.root = tree.insert(tree.root, 30)
    # Print the tree in-order
    tree.in_order_traversal(tree.root)
