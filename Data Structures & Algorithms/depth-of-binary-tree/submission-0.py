class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = []
        res = 0
        if root:
            s.append([root, 1])

        while s:
            node, level = s.pop()
            if node:
                res = max(res, level)
                s.append([node.left, level + 1])
                s.append([node.right, level + 1])
        return res