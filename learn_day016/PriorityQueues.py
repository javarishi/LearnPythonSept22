import queue

customers = queue.PriorityQueue()

customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))
customers.put((8, "David"))

print(customers.qsize())
while customers:
    print(customers.get())