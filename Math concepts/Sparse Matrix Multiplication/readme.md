# Sparse matrix multiplication

**Task**: Write a function that takes in two integer matrices and multiplies them together.

Both matrices will be sparse, meaning that most of their elements will be zero. Take advantage of that to reduce the number of total computations that your function performs.

If the matrices can't be multiplied together, your function should return  ``` [[]] ```.

**Sample Input:**
```
matrix_a = [
[0,  2, 0],
[0, -3, 5],
]
matrix_b = [
[0, 10, 0],
[0,  0, 0],
[0,  0, 4],
]
```
**Sample Output**
```
[
[0, 0,  0],
[0, 0, 20],
]
```