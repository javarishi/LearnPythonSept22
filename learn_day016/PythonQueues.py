# Data in Queues is always FIFO - First In, First Out
import queue
# test_queue = queue.Queue()
simpleQueue = queue.SimpleQueue() # Normal FIFO queue
priorityQueue = queue.PriorityQueue() # Priority of messages is respected
lifoQueue = queue.LifoQueue() # Last In First Out

for i in range(1,11):
    simpleQueue.put("Message {}".format(i))
    priorityQueue.put("Message {}".format(i))
    lifoQueue.put("Message {}".format(i))
print("Messages are added into all queues")

print("Size of SimpleQueue" , simpleQueue.qsize())
print("Size of PriorityQueue" , priorityQueue.qsize())
print("Size of LifoQueue" , lifoQueue.qsize())

print("Message from SimpleQueue ", simpleQueue.get())
print("Message from PriorityQueue ", priorityQueue.get())
print("Message from LifoQueue ", lifoQueue.get())