class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


def sumTwoLL(head1: ListNode, head2: ListNode) -> ListNode:

    if head1 is None:
        return None
    if head2 is None:
        return None

    curr1, curr2 = head1, head2
    sentinel = ListNode(0)
    node = sentinel

    while curr1 or curr2:

        result = 0
        if curr1:
            result += curr1.value
            curr1 = curr1.next
        if curr2:
            result += curr2.value
            curr2 = curr2.next
        node.next = ListNode(result)
        node = node.next
    return sentinel.next
    



# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(5)))
LL2 = ListNode(-1, ListNode(3, ListNode(-10)))
print(arrayify(sumTwoLL(LL1, LL2))) # [0, 6, -5]
print(arrayify(sumTwoLL(ListNode(0), ListNode(0)))) # [0]
print(sumTwoLL(None, None)) # None







# Given two linked lists of equal length, sum elements' value at the same position.

# Examples:
# • Given two linked lists: 1 ➞ 3 ➞ 5 and -1 ➞ 3 ➞ -10 // returns 0 ➞ 6 ➞ -5
# • Given two linked lists: 0 and 0 // returns 0