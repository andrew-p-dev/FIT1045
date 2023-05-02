# https://leetcode.com/problems/invert-binary-tree/

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.helper(root.left, root.right)
        return root
    
    def helper(self, left, right):
        if left is None:
            return
        left.val, right.val = right.val, left.val
        if left.left:
            self.helper(left.left, right.right)
            self.helper(left.right, right.left)