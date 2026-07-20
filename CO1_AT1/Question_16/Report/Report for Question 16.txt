# Question 16: Case-Based Analysis of Algorithm Efficiency Using Merge Sort

## Objective

The objective of this experiment is to analyze the efficiency of the Merge Sort algorithm under different input conditions. The analysis includes the best, average, and worst-case scenarios using asymptotic notations and compares their performance. The experiment also identifies which case is most relevant in practical applications.

## Introduction

Merge Sort is a comparison-based sorting algorithm that follows the Divide and Conquer strategy. It recursively divides an array into smaller subarrays until each subarray contains a single element. These subarrays are then merged in sorted order to produce the final sorted array. Merge Sort is widely used because it guarantees efficient performance regardless of the initial order of the input data.

## Algorithm

1. Divide the array into two equal halves.
2. Recursively apply Merge Sort to each half.
3. Merge the sorted halves into a single sorted array.
4. Repeat until the complete array is sorted.

## Input

Sample Array:

```
[45, 12, 67, 23, 89, 10, 5]
```

## Output

Sorted Array:

```
[5, 10, 12, 23, 45, 67, 89]
```

## Complexity Analysis

| Case         | Input Condition | Time Complexity |
| ------------ | --------------- | --------------- |
| Best Case    | Already Sorted  | O(n log n)      |
| Average Case | Random Order    | O(n log n)      |
| Worst Case   | Reverse Sorted  | O(n log n)      |

### Space Complexity

**O(n)** because Merge Sort requires additional memory for merging the divided arrays.

## Asymptotic Notations

* **Big-O:** O(n log n)
* **Big-Theta:** Θ(n log n)
* **Big-Omega:** Ω(n log n)

## Comparison Table

| Scenario | Performance |
| -------- | ----------- |
| Best     | O(n log n)  |
| Average  | O(n log n)  |
| Worst    | O(n log n)  |

## Practical Relevance

In real-world applications, the average-case scenario is the most significant because data is usually unsorted. Merge Sort provides consistent performance regardless of the input arrangement, making it suitable for database systems, operating systems, and large-scale applications.

## Analysis

The execution results show that Merge Sort maintains the same time complexity in all three cases. Unlike simple sorting algorithms, its efficiency is not affected by whether the input data is already sorted or completely reversed. This predictable behavior makes Merge Sort one of the most reliable comparison-based sorting algorithms.

## Conclusion

Merge Sort is an efficient and stable sorting algorithm with a guaranteed time complexity of **O(n log n)** in the best, average, and worst cases. Although it requires additional memory, its consistent performance makes it an excellent choice for sorting large datasets.

## Screenshots to Include

* Screenshot of the Python source code
* Screenshot of the program output
* Complexity comparison table
* Complexity chart (Best vs Average vs Worst)
