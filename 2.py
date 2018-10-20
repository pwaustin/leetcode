class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    Problem:
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
    order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode

    Solution:
    Until the linked lists are exhausted simply sum digit by digit, handling the carry from the previous digit as
    necessary.
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

