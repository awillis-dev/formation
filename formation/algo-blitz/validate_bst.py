
class TreeNode:
  def __init__(self, value = 0, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

def validateBST(root: TreeNode, min = float('-inf'), max = float('inf')):
  if root is None:
    return True
  if root.value <= min or root.value >= max:
    return False
  
  return validateBST(root.left, min, root.value) and validateBST(root.right, root.value, max)

tree1 = TreeNode(2, TreeNode(1), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
tree3 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10, None, TreeNode(14, TreeNode(13))))

print(validateBST(tree1)) # True


