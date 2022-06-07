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

def append(node, target):
      
  if node is None:
    return ListNode(target)

  curr = node
  while curr.next:
    curr = curr.next
  curr.next = ListNode(target)
  return node



#  Given a linked list, append an element with a target value to the list iteratively.

# Examples:
# • Given a linked list: 1 ➞ 4 ➞ 5, target: 7 // returns 1 ➞ 4 ➞ 5 ➞ 7
# • Given a linked list: 0, target 7 // returns 0 ➞ 7


# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(arrayify(append(None, 1))) # [1]
print(arrayify(append(LL1, 7))) # [1, 4, 5, 7]
print(arrayify(append(ListNode(), 7))) # [0, 7]