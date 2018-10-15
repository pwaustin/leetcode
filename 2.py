class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    result_head = ListNode(0)
    current = result_head
    while l1 or l2:
        this_digit = carry
        if l1:
            this_digit += l1.val
            l1 = l1.next
        if l2:
            this_digit += l2.val
            l2 = l2.next
        if this_digit > 9:
            carry = 1
            this_digit -= 10
        else:
            carry = 0
        current.next = ListNode(this_digit)
        current = current.next
    if carry == 1:
        current.next = ListNode(1)
    return result_head.next

