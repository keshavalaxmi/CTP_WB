# Exercise 2: 0/1 Knapsack using Dynamic Programming

## Objective

Implement Dynamic Programming for the 0/1 Knapsack problem and analyze its time and space complexity.

## Input

Weights of items:

[2, 3, 4, 5]

Values of items:

[3, 4, 5, 6]

Knapsack Capacity:

5

## Output

Maximum Profit:

7

## Algorithm

1. Initialize a DP table with rows representing items and columns representing capacities.
2. Set all values in the DP table to 0 initially.
3. For each item, check every possible capacity from 1 to the given capacity.
4. If the weight of the current item is less than or equal to the current capacity, consider two choices:
   - Include the current item.
   - Exclude the current item.
5. Store the maximum value of these two choices in the DP table.
6. If the item's weight is greater than the current capacity, exclude the item.
7. The final cell of the DP table contains the maximum profit.

## Time Complexity

O(nW)

where:
- n = number of items
- W = knapsack capacity

## Space Complexity

O(nW)

where:
- n = number of items
- W = knapsack capacity

## Program

The implementation is available in `knapsack.py`.
