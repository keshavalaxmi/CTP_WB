# Exercise 7: Producer-Consumer Application

## Objective

Develop a Producer-Consumer application using threading, multiprocessing and synchronization primitives.

## Concepts Used

- Threading
- Multiprocessing
- Producer-Consumer
- Queue
- Synchronization
- `threading.Thread`
- `multiprocessing.Process`
- `queue.Queue`
- `multiprocessing.Queue`

## Description

The Producer-Consumer problem consists of a producer that generates data and a consumer that processes the data.

The program implements the Producer-Consumer model using both threading and multiprocessing.

## Algorithm

1. Import the required Python modules.
2. Create a queue to store the produced items.
3. Define a producer to add items to the queue.
4. Define a consumer to remove items from the queue.
5. Create and start producer and consumer threads.
6. Wait for both threads to complete.
7. Create a multiprocessing queue.
8. Create producer and consumer processes.
9. Start both processes and wait for them to complete.
10. Display the produced and consumed items.

## Input

Numbers from 1 to 5.

## Output

The producer produces the numbers and the consumer consumes them using threading and multiprocessing.

## Time Complexity

O(n)

where n is the number of items produced.

## Space Complexity

O(n)

where n is the number of items stored in the queue.

## Result

The Producer-Consumer application was successfully implemented using threading, multiprocessing, and synchronization primitives.

## Program

The implementation is available in `producer_consumer.py`.
