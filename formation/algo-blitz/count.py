class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
    
def count(node):
  curr = node
  count = 0
  
  if curr is None:
    return 0
  while curr:
    count += 1
    curr = curr.next
  return count
    
  
  
# Test Case
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None)) # 0
print(count(LL1)) # 3
print(count(ListNode())) # 1