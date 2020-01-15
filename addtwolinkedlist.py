
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def addlinkedlist(self, l1, l2):

        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:

            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, ls_digit = divmod(v1+v2+carry, 10)
            n.next = ListNode(ls_digit)
            n = n.next

        return root.next

    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)

        while l1 and l2:

            if l1.val < l2.val:
                cur.next = l1.val
                l1 = l1.next

            else:
                cur.next = l2.val
                l2 = l2.next

            cur = cur.next

        cur.next = l1 or l2
        return dummy.next

    def reverseKGroup(self, head, k):

        node = head
        count = 0
        while node and count < k:
            node = node.next
            count +=1
        if count < k:
            return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev



    def reverse(self, head, count):
        cur = head
        prev = None
        next = None

        while count > 0:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next
            count -=1

        return (cur, prev)