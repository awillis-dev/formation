class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def DFSTree(root: TreeNode, target: int) -> bool:
    # Write your code here.
    pass


# Test Cases
tree1 = TreeNode(
    3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9)))
)
print(DFSTree(None, 1))  # False
print(DFSTree(tree1, 9))  # True
print(DFSTree(tree1, 1))  # False
print(DFSTree(tree1, 2))  # True
print(DFSTree(TreeNode(1), 2))  # False
