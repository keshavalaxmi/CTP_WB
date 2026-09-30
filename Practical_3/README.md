# Exercise 3: Stack and Queue

## Objective

Develop a reusable Python package implementing Stack and Queue using type hints and dataclasses.

## Stack

A Stack follows the LIFO (Last In, First Out) principle.

### Operations

- `push()` - Adds an element to the top of the stack.
- `pop()` - Removes and returns the top element from the stack.

## Queue

A Queue follows the FIFO (First In, First Out) principle.

### Operations

- `enqueue()` - Adds an element to the rear of the queue.
- `dequeue()` - Removes and returns the front element from the queue.

## Algorithm

### Stack

1. Initialize an empty stack using a dataclass.
2. Use `push()` to add elements to the stack.
3. Use `pop()` to remove the last inserted element.
4. Display the stack and the popped element.

### Queue

1. Initialize an empty queue using a dataclass.
2. Use `enqueue()` to add elements to the queue.
3. Use `dequeue()` to remove the first inserted element.
4. Display the queue and the dequeued element.

## Output

```text
Stack: [10, 20, 30]
Popped: 30
Queue: [10, 20, 30]
Dequeued: 10
