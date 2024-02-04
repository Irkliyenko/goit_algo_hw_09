In this analysis, I compared the performance of two algorithms: the greedy algorithm and dynamic programming. I utilized the coin problem, where the algorithm is tasked with finding the smallest number of coins needed to reach a specified amount, price, or change. First, I compared the results obtained from these algorithms, acknowledging that the greedy algorithm tends to choose local optima and may not always yield the global optimum. In contrast, dynamic programming builds a table—in my case, two lists—with all the results and selects the global optimum based on this table. As depicted in Table 1, there's no discernible difference in results for this specific problem.

**Table 1: Search Results for Dynamic Programming and Greedy Algorithm.**

| Algorithm | Amount: 100 | Amount: 325 | Amount: 769 | Amount: 1428 |
| --------- | ----------- | ----------- | ----------- | ------------ | ----- | ---- | ---- | ------ | ----- | ---- | ---- |
| Dynamic   | 50: 2       | 50: 6       | 25: 1       | 50: 15       | 10: 1 | 5: 1 | 2: 2 | 50: 28 | 25: 1 | 2: 1 | 1: 1 |
| Greedy    | 50: 2       | 50: 6       | 25: 1       | 50: 15       | 10: 1 | 5: 1 | 2: 2 | 50: 28 | 25: 1 | 2: 1 | 1: 1 |

Next, I compared the time required for each algorithm to complete their tasks, as shown in Table 2. Specifically, for this task, the greedy algorithm significantly outperformed dynamic programming, and the time difference increased with higher amounts. For instance, for an amount of 100, the greedy algorithm was 91 times faster, while for an amount of 1428, the speed difference increased to 318 times. This performance gap can be attributed to the dynamic programming table creation. The time complexity of the dynamic programming algorithm for the coin change problem is O(nm), where n is the amount and m is the number of different coin denominations. While for the greedy algorithm it is O(n).

**Table 2: Searching Performancce of Dynamic Programing and Greedy Algorithm.**

| Algorithm | Amount: 100 | Amount: 325 | Amount: 769 | Amount: 1428 |
| --------- | ----------- | ----------- | ----------- | ------------ |
| Dynamic   | 0.02543     | 0.08463     | 0.21054     | 0.38973      |
| Greedy    | 0.00028     | 0.00043     | 0.00085     | 0.00122      |

Based on these results, it can be concluded that the greedy algorithm performed better for this task. However, it is crucial to remember that the greedy algorithm does not always provide the optimal result, whereas dynamic programming consistently delivers the best solution.
