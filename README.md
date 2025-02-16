# PT2-DAA-JARILLA
This is my Task Performance 2 for Design and Analysis of Algorithms
The files includes, the codes as well as the link for the Video Presentation part.

1) Divide and Conquer - Merge Sort Example
Explanation: Merge Sort is a classic divide-and-conquer algorithm. It splits the array into two halves, recursively sorts each half, and then merges the sorted halves. This approach ensures a time complexity of O(n log n).

Code explanation/Introduction: The merge_sort function recursively divides the array, and the merge function combines the sorted halves.

2) Dynamic Programming - Fibonacci Example (Memoization)
Explanation: Dynamic Programming optimizes recursive problems by storing intermediate results (memoization). This avoids redundant calculations, reducing the Fibonacci sequence's time complexity from O(2^n) to O(n).

Code explanation/Introduction: The fibonacci function uses a memo dictionary to store previously computed Fibonacci numbers.

3) Greedy Algorithm - Coin Change Problem
Explanation: Greedy algorithms make locally optimal choices at each step. For the coin change problem, it selects the largest possible coin first to minimize the total number of coins. However, this approach doesn’t always guarantee the optimal solution.

Code explanation/Introduction: The min_coins function sorts the coins in descending order and iteratively subtracts the largest possible coin from the amount.

4) Backtracking - Simple N-Queens Example (4x4 Board)
Explanation: Backtracking systematically explores all possible solutions by trying out choices and undoing them if they lead to a dead end. The N-Queens problem places queens on a chessboard so that no two queens threaten each other.

Code explanation/Introduction: The solve_n_queens function uses backtracking to place queens row by row and checks for conflicts using the is_safe function.

5) Branch & Bound - 0/1 Knapsack Problem (Basic Example)
Explanation: Branch and Bound is an optimization technique that explores all possible solutions but prunes branches that cannot lead to a better solution than the current best. The 0/1 Knapsack problem maximizes the value of items in a knapsack without exceeding its capacity.

Code explanation/Introduction: The knapsack_branch_bound function uses recursion to explore all combinations of items and prunes invalid branches.

6) Recursion - Factorial Calculation
Explanation: Recursion solves problems by breaking them into smaller instances of the same problem. The factorial of a number n is computed as n * factorial(n - 1).

Code explanation/Introduction: The factorial function calls itself with a smaller input until it reaches the base case (n == 0).

7) Heuristic Method - Traveling Salesman Approximation
Explanation: Heuristic methods provide approximate solutions to hard problems like the Traveling Salesman Problem (TSP). The Nearest Neighbor heuristic builds a tour by always visiting the nearest unvisited city.

Code explanation/Introduction: The nearest_neighbor_tsp function constructs a tour by iteratively selecting the closest city.

8) Randomized Algorithm - QuickSort (Random Pivot)
Explanation: Randomized algorithms use randomness to improve efficiency or simplify implementation. QuickSort selects a random pivot to partition the array, ensuring an average time complexity of O(n log n).

Code explanation/Introduction: The quicksort function recursively sorts elements smaller and larger than the pivot.

9) Transform and Conquer - Binary Search
Explanation: Transform and Conquer simplifies problems by transforming the input. Binary Search works on sorted arrays by repeatedly dividing the search interval in half, achieving a time complexity of O(log n).

Code explanation/Introduction: The binary_search function narrows down the search range by comparing the target with the middle element.

GDRIVE LINK: https://drive.google.com/drive/folders/104JT7ctfv8nHaiI529RzDxqxyd8_7DHW?usp=drive_link 


