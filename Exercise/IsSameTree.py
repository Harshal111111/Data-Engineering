class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    # Base case: If both nodes are None, the trees are the same
    if not p and not q:
      return True

    # If one of the nodes is None, or the values are different, they are not the same
    if not p or not q or p.val != q.val:
      return False

    # Recursively check the left and right subtrees
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Example usage:
# Tree 1:       Tree 2:
#    1             1
#   / \           / \
#  2   3         2   3
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

sol = Solution()
print(sol.isSameTree(p, q))  # Output: True
