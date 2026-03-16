class StackFrontier:
    def __init__(self):
        # frontier elemanlarının listesi
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if len(self.frontier) == 0:
            raise Exception("Frontier boş")

        # LIFO, son giren ilk çıkar
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if len(self.frontier) == 0:
            raise Exception("Frontier boş")

        # FIFO, ilk giren ilk çıkar
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node


# TEST 
print("STACK TEST (LIFO)")
stack = StackFrontier()

stack.add("X")
stack.add("Y")
stack.add("Z")

print(stack.remove())
print(stack.remove())
print(stack.remove())


print("\nQUEUE TEST (FIFO)")
queue = QueueFrontier()

queue.add("X")
queue.add("Y")
queue.add("Z")

print(queue.remove())
print(queue.remove())
print(queue.remove())