 class ListNode:
  def __init__(self, value = 0, next = None): 
    self.value = value
    self.next = next
    
def sum(node): 
  if not node: 
    return 0
  else:
    return node.value + sum(node.next)


# Test Cases
LL1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
LL2 = ListNode(1, ListNode(4, ListNode(3)))

print(sum(None)) # 0
print(sum(LL1)) # 10
print(sum(LL2)) # 8
print(sum(ListNode())) # 1