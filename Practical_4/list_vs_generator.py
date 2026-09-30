import time
import tracemalloc

n = 100000

# List
tracemalloc.start()
start = time.time()

numbers = [i * i for i in range(n)]

list_time = time.time() - start
list_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()


# Generator
tracemalloc.start()
start = time.time()

numbers = (i * i for i in range(n))

for x in numbers:
    pass

generator_time = time.time() - start
generator_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("List Time:", list_time)
print("List Memory:", list_memory)
print("Generator Time:", generator_time)
print("Generator Memory:", generator_memory)
