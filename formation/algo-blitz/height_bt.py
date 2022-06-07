class TreeNode:
  def __init__(self, value = 0, left = None, right = None):
      self.value = value
      self.left = left
      self.right = right

def findTreeHeight(root: TreeNode):
  if root is None:
    return 0
  
  left_height = findTreeHeight(root.left)
  right_height = findTreeHeight(root.right)
  
  return max(left_height, right_height) + 1

# print(findTreeHeight(None)) # -1
print(findTreeHeight(TreeNode(1, TreeNode(2), TreeNode(3)))) # 1
# print(findTreeHeight(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9)))))) # 3
# print(findTreeHeight(TreeNode())) # 0
