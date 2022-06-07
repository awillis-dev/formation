class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

def search(head, target):
  curr = head
  
  if curr is None:
    return False
  
  while curr:
    if curr.value == target:
      return True
    curr = curr.next
  return False
  
# Test Cases
LL1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(6, ListNode(7, ListNode(10)))))))
print(search(None, 1)) # False
print(search(LL1, 2)) # True
print(search(LL1, 4)) # False
print(search(LL1, -1)) # False
print(search(LL1, 10)) # True
print(search(LL1, 11)) # False



# recursive
def search(head: Node, target: int) -> bool: 
  # if not head:
  #   return False
  # return head.value == target or search(head.next, target)