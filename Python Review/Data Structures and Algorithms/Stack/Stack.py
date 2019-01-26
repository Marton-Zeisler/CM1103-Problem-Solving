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
			
	def insertFirst(self, node):
		node.next = self.head
		self.head = node
		
	def deleteFirst(self):
		if self.head:
			deletedNode = self.head
			self.head = self.head.next
			return deletedNode
		else:
			return None
			

class Stack:
	def __init__(self, top=None):
		self.linkedList = LinkedList(top)
	
	def push(self, node):
		self.linkedList.insertFirst(node)
		
	def pop(self):
		return self.linkedList.deleteFirst()
		
		
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

stack = Stack(node1)
stack.push(node2)
print(stack.pop().value)
stack.push(node3)
stack.push(node4)
print(stack.pop().value)
print(stack.pop().value)