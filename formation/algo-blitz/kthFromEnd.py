class ListNode:
  def __init__(self, value = 0, next = None): 
    self.value = value
    self.next = next

def kthFromLast(head,k):
  
  if head is None:
    return None
  
  slow = head
  fast = head.next
  
  for i in range(k):
    if fast is None:
      return -1
    else:
      fast = fast.next
  
  while fast:
    fast = fast.next
    slow = slow.next
  return slow.value



# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print(kthFromLast(LL1, 0)) # 10
print(kthFromLast(LL1, 2)) # 3
print(kthFromLast(LL1, 5)) # 13
print(kthFromLast(LL1, 6)) # -1