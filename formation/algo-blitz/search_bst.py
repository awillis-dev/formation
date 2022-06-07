class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def searchBST(root: TreeNode, target: int):
    curr = root
    while curr:
      if curr.value == target:
        return curr
      if curr.value < target:
        curr = curr.right
      if curr.value > target:
        curr = curr.left
    return False

# Test Cases
tree = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10, None, TreeNode(14, TreeNode(13))))
print(searchBST(None, 1)) # False
print(searchBST(tree, 1)) # True
print(searchBST(tree, 14)) # True
print(searchBST(tree, 2)) # False
print(searchBST(tree, 13)) # True
print(searchBST(TreeNode(), 0)) # True