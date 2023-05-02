# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root.left, root.right, True)
        return root
    
    def helper(self, left, right, isOdd):
        if left is None:
            return
        if isOdd:
            left.val, right.val = right.val, left.val
        if left.left:
            self.helper(left.left, right.right, not isOdd)
            self.helper(left.right, right.left, not isOdd)
        