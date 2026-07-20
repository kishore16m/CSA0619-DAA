# Question 40: Application of Master Theorem in Genome Sequencing Analysis

## Objective

The objective of this experiment is to determine the time complexity of the recurrence relation used in a genome sequencing algorithm by applying the Master Theorem and analyzing its scalability for large biological datasets.

## Problem Statement

The recurrence relation is given as:

**T(n) = 3T(n/2) + n**

The task is to determine its time complexity using the Master Theorem and explain how the algorithm performs as the dataset size increases.

## Master Theorem

The general form of the Master Theorem is:

**T(n) = aT(n/b) + f(n)**

Comparing with the given recurrence:

* **a = 3**
* **b = 2**
* **f(n) = n**

Calculate:

**log₂3 ≈ 1.585**

Since:

**f(n) = n = O(n^(1.585 − ε))**

for some ε > 0, the recurrence satisfies **Case 1** of the Master Theorem.

## Time Complexity

**Θ(n^log₂3)**

Approximately,

**Θ(n^1.585)**

## Scalability Analysis

| Dataset Size           | Performance                      |
| ---------------------- | -------------------------------- |
| Small                  | Fast execution                   |
| Medium                 | Moderate execution time          |
| Large                  | Efficient and scalable           |
| Very Large Genome Data | Better than quadratic algorithms |

## Analysis

Genome sequencing involves processing extremely large biological datasets containing millions or billions of DNA base pairs. An algorithm with a time complexity of **Θ(n^1.585)** grows significantly slower than quadratic algorithms, making it suitable for large-scale genomic analysis. As the dataset size increases, the execution time increases at a manageable rate, ensuring good scalability.

## Conclusion

By applying the Master Theorem, the recurrence relation **T(n) = 3T(n/2) + n** satisfies **Case 1**, resulting in a time complexity of **Θ(n^1.585)**. This complexity demonstrates that the algorithm scales efficiently for genome sequencing applications and performs much better than algorithms with quadratic complexity.

## Screenshots to Include

* Screenshot of the Python source code
* Screenshot of the program output
* Master Theorem calculation
* Scalability comparison table
* Complexity chart
