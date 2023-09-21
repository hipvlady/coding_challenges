# Get Statistics

### Category: Math Concepts

Write a function that takes in a list of numbers and returns a dictionary containing the following statistics 
about the numbers: the mean, median, mode, sample variance, sample standard deviation, and 95% confidence 
interval for the mean.

Note that:

- You can assume that the given list contains a large-enough number of samples from a population to use a z-score of 1.96.
- If there's more than one mode, your function can return any of them.
- You shouldn't use any libraries.
- Your output values will automatically be rounded to the fourth decimal.

**Sample Input**
```
input_list = [2, 1, 3, 4, 4, 5, 6, 7]
```
**Sample Output**
```
{
"mean": 4.0,
"median": 4.0,
"mode": 4.0,
"sample_variance": 4.0,
"sample_standard_deviation": 2.0,
"mean_confidence_interval": [2.6141, 5.3859],
}
```

Hints:

- Hint 1: The mean is the sum of the values divided by the number of values.
- Hint 2: The median is the middle value of the sorted values. If the input list has an even number of elements, the median is the average of the two middle values. Naturally, you'll first have to sort the input list, and you'll then have to find the middle index (or the two middle indices if the list has an even number of elements).
- Hint 3: The mode is the most frequent element in the input list. You'll have to count how many times each value appears in the list.
- Hint 4: Sample Variance. Average of the squared differences from the mean.