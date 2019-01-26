class Queue:
	def __init__(self, head=None):
		self.storage = [head]
	
	def enqueue(self, newElement):
		self.storage.append(newElement)
		
	def peek(self):
		return self.storage[0]
		
	def dequeue(self):
		return self.storage.pop(0)
		
		
queue = Queue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())