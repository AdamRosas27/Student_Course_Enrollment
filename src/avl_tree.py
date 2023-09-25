from course import Course

# Add a class that will represent the AVL tree and its methods
### AVL Tree stucture given by professor Celly translated from Java to Python ###


class Node:
    def __init__(self, course):
        self.course = course
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, root, course):
        if not root:
            return Node(course)
        if course.start_time < root.course.start_time:
            root.left = self.insert(root.left, course)
        elif course.start_time > root.course.start_time:
            root.right = self.insert(root.right, course)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and course.start_time < root.left.course.start_time:
            return self.right_rotate(root)
        if balance < -1 and course.start_time > root.right.course.start_time:
            return self.left_rotate(root)
        if balance > 1 and course.start_time > root.left.course.start_time:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and course.start_time < root.right.course.start_time:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.course.course_name, end=" ")
            self.in_order_traversal(node.right)
