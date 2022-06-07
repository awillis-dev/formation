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

def remove(node, target): 
  sentinel = ListNode(0)
  sentinel.next = node
  
  curr = sentinel
  while curr.next:
    if curr.next.value == target:
      curr.next = curr.next.next
    else:
      curr = curr.next
  return sentinel.next
  
# Test Cases
LL1 = ListNode(4, ListNode(2, ListNode(1, ListNode(1, ListNode(3, ListNode(2, ListNode(2)))))))
LL2 = remove(None, 1)
print(arrayify(LL2)) # []
LL1 = remove(LL1, 1)
print(arrayify(LL1)) # [4, 2, 3, 2, 2]
LL1 = remove(LL1, 2)
print(arrayify(LL1)) # [4, 3]
remove(LL1, 3)
print(arrayify(LL1)) # [4]
LL1 = remove(LL1, 4)
print(arrayify(LL1)) # []
