class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        output = []
        while queue:
            num = len(queue)
            temp = []
            while num:
                cur = queue.pop(0)
                # output.append(cur.val)
                temp.append(cur.val)
                # 这里注意，N叉树默认子节点是以列表形式给出的
                queue.extend(cur.children)
                num -= 1
            output.append(temp)
        return output