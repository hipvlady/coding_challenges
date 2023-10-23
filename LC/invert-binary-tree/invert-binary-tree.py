
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    """
    def invertBinaryTree(self, tree):
        queue = tree
        while len(queue):
            current = queue.pop(0)
            if current is None:
                continue
            self.swapLeftAndRight(current)
            queue.append(current.left)
            queue.append(current.right)

    def swapLeftAndRight(self, tree):
        tree.left, tree.right = self.left, self.right

    """

    def invertBinaryTree(self, tree):
      if tree is None:
        return []
      self.swapLeftAndRight(tree.left)
      self.invertBinaryTree(tree.right)

    def swapLeftAndRight(self, tree):
      tree.left, tree.right = self.left, self.right