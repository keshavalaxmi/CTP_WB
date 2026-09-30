# Exercise 4: List-Based Processing vs Generator-Based Processing

## Objective

Compare list-based processing and generator-based processing for a large dataset in terms of execution time and memory usage.

## Input

A large dataset of 100,000 numbers.

The program calculates the square of each number.

## Method

### List-Based Processing

A list comprehension is used to calculate and store all the squared values in memory.

### Generator-Based Processing

A generator expression is used to generate the squared values one at a time.

## Algorithm

1. Set the dataset size to 100,000.
2. Start memory tracking using `tracemalloc`.
3. Measure the execution time for list-based processing.
4. Record the peak memory used by the list.
5. Stop memory tracking.
6. Start memory tracking again.
7. Measure the execution time for generator-based processing.
8. Iterate through the generator.
9. Record the peak memory used by the generator.
10. Display the execution time and memory usage for both approaches.

## Expected Result

The list generally uses more memory because all values are stored in memory at once.

The generator generally uses much less memory because values are generated one at a time.

Execution time may vary depending on the system and Python environment.

## Time Complexity

Both approaches process `n` elements.

- List: O(n)
- Generator: O(n)

## Space Complexity

- List: O(n)
- Generator: O(1) additional space

## Program

The implementation is available in `list_vs_generator.py`.
