#author：张思选
#email：1057950343@qq.com
#class ListNode:
#    def __init__(self,x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        current = root
        carry = 0
        while l1 or l2:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            tmp = ListNode(val)
            current.next = tmp
            current = current.next
        if carry:
            tmp = ListNode(carry)
            current.next = tmp
        return root.next
