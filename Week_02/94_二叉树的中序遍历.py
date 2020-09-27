class Solution:
    def inorderTraversal(self, root):
        stack = [root]
        output = []
        cur = stack.pop()
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            output.append(cur.val)
            # stack.append(cur.right)
            # cur = stack.pop()
            cur = cur.right
        return output
        