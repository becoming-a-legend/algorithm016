class Solution:
    def preorderTraversal(self, root):
        # 迭代
        stack = [root]
        cur = stack.pop()
        output = []
        while cur or stack:
            while cur:
                output.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            # stack.append(cur.right)
            cur = cur.right
        return output