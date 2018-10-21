class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def odd_even_list(head):
    """
    Problem:
    Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
    about the node number and not the value in the nodes. You should try to do it in place. The program should run in
    O(1) space complexity and O(nodes) time complexity.

    :type head: ListNode
    :rtype: ListNode

    Solution:
    Restitch the pointers as we go, maintaining whether the current node is even or odd and appending it to the
    appropriate list. When finished, point the end of the odd list at the start of the even list and make sure the end
    of the even list points to nothing.
    """

    if not head:
        return None

    odd_start = head
    odd_current = head
    current = head

    if current.next:
        current = current.next
        even_start = current
        even_current = current
    else:
        return head

    is_odd = False

    while current.next:
        current = current.next
        is_odd = not is_odd
        if is_odd:
            odd_current.next = current
            odd_current = current
        else:
            even_current.next = current
            even_current = current

    odd_current.next = even_start
    even_current.next = None

    return odd_start
