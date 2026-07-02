class TreeNode:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
root = TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(15)
root.left.left=TreeNode(100)
root.left.right=TreeNode(120)
print("root code", root.value)
print("left child node root.left.value)
print(root.right.value)
print(root.left.left.value)
print(root.left.right.value)