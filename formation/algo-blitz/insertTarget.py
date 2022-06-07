# iterative

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

def insert(head, target):
	curr = head

	if curr is None:
		return ListNode(target,head)

	if target < curr.value:
			# new_node = ListNode(target)
			# new_node.next = curr
			# return new_node
		return ListNode(target,head)

	while curr.next and target > curr.next.value:
		curr = curr.next

	new_node = ListNode(target)
	new_node.next = curr.next
	curr.next = new_node

	return head


# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(4)))
LL2 = ListNode(-3, ListNode(-2, ListNode(-1)))

print(arrayify(insert(LL1, 2))) # [1, 2, 3, 4]
print(arrayify(insert(LL2, -4))) # [-4, -3, -2, -1]
print(arrayify(insert(LL2, 0))) # [-3, -2, -1, 0]
print(arrayify(insert(None, 1))) # [1]
