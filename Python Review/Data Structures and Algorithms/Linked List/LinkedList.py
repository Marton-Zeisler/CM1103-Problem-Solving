class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		
class LinkedList:
	def __init__(self, head=None):
		self.head = head
	
	def addNode(self, node):
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = node
		else:
			self.head = node
			
	def get_position(self, position):
		if position < 1 or self.head == None:
			return None
		
		counter = 1
		current = self.head
		while current and counter <= position:
			if counter == position:
				return current
			current = current.next
			counter += 1
		
		return None
		
	def insert(self, node, position):
		if position > 1:
			counter = 1
			current = self.head
			while current and counter < position:
				if counter == position - 1:
					node.next = current.next
					current.next = node
					return
				else:
					current = current.next
					counter += 1
		elif position == 1:
			node.next = self.head
			self.head = node
	
	def delete(self, value):
		prev = None
		current = self.head
		
		while current.value != value and current.next:
			prev = current
			current = current.next
		
		if current.value == value:
			if prev:
				prev.next = current.next
			else:
				self.head = current.next
				
				
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

linkedList = LinkedList(n1)
linkedList.addNode(n2)
print(linkedList.get_position(2).value)

linkedList.insert(n3, 2)
print(linkedList.get_position(2).value)

linkedList.delete(1)
print(linkedList.get_position(2).value)