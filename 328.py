class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def odd_even_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
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
