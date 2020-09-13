class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 解法一, 构建一个头节点，用来梳理两个链表
        # head = ListNode(0)
        # node = head
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         node.next = l1
        #         node = l1
        #         l1 = l1.next            
        #     else:
        #         node.next = l2
        #         node = l2
        #         l2 = l2.next
        # if l1:
        #     node.next = l1
        # else:
        #     node.next = l2
        
        # return head.next
        

        # 解法二， 直接在两个链表上操作
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # if l1.val <= l2.val:
        #     node = l1
        # else:
        #     node = l2
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         while l1 and l1.val <= l2.val:
        #             temp = l1
        #             l1 = l1.next
        #         temp.next = l2
        #     else:
        #         while l2 and l1.val > l2.val:
        #             temp = l2
        #             l2 = l2.next
        #         temp.next = l1
        
        # return node


        # 子问题很明显，递归 
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
  
            
