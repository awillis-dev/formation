class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

def arrayify(head):
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

def reverse(head):
    p1, p2 = None, head
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1


# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))

# print((reverse(ListNode(1)))) # [1]
listA = print(arrayify(reverse(ListNode(1)))) # [1]
listB = print(arrayify(reverse(ListNode(1, ListNode(2))))) # [2, 1]
listC = print(arrayify(reverse(LL1))) # [10, 7, 3, 5, 1, 13]