class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

def findMiddle(head: ListNode) -> int:

    if head is None:
        return None

    slow = head
    fast = head.next

    while fast and fast.next:

        fast = fast.next.next
        slow = slow.next

    return slow.value


# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(5)))
LL2 = ListNode(1, ListNode(3, ListNode(-13, ListNode(-3, ListNode(1)))))
LL3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
LL4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

print(findMiddle(None)) # None
print(findMiddle(LL1)) # 3
print(findMiddle(LL2)) # -13
print(findMiddle(LL3)) # 2
print(findMiddle(LL4)) # 3
print(findMiddle(ListNode(1))) # 1


# Q. Given a linked list, find the middle element in one pass. If the length of the list is even, return the first of the two middle nodes.

# Examples:
# • Given a linked list: 1 ➞ 3 ➞ 5 // returns 3
# • Given a linked list:  1 ➞ 2 ➞ 3 ➞ 4 // returns 2