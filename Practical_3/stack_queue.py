from dataclasses import dataclass, field

@dataclass
class Stack:
    items: list = field(default_factory=list)

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()


@dataclass
class Queue:
    items: list = field(default_factory=list)

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)


# Stack
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.items)
print("Popped:", s.pop())

# Queue
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:", q.items)
print("Dequeued:", q.dequeue())
