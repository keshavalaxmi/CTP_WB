# Exercise 1: Merge Sort

## Objective

Implement the Divide-and-Conquer algorithm for Merge Sort and calculate its time and space complexities.

## Input

A list of unsorted numbers:

[38, 27, 43, 3, 9, 82, 10]

## Output

A sorted list of numbers in ascending order:

[3, 9, 10, 27, 38, 43, 82]

## Algorithm

1. Check if the length of the array is 1 or less. If yes, return the array.
2. Find the middle position of the array.
3. Divide the array into two halves.
4. Recursively apply Merge Sort to both halves.
5. Merge the two sorted halves together.
6. Return the sorted array.

## Time Complexity

O(n log n)

## Space Complexity

O(n)

## Program

The implementation is available in `merge_sort.py`.
