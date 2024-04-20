# Comparing 2 lists of strings and extracting similar names

## Description:

### Summary:

> This project aims to differentiate between 2 lists of companies and extract the names of companies which are similar between them.
> The catch is that some of the names might be misspelled.

### Tools used:

1. Python

### Methodology:

To determine whether the companies are considered similar we will:

1. First extract the names which are exactly the same between the 2 lists
2. Secondly, extract names which are substrings of a name in the other list
3. Thirdly, calculate the Levenshtein distance function from the textdistance module and include the names if the similarity score >0.9 (arbitrary cut off)
4. Lastly, check if there are names which are substrings of another found name within the same list. The reason this step is required is because the time required for Step 3 is large, hence once a match has been found, the loop moves on to the next name

#### Input:

Raw CSV file with the 2 lists of company names in separate columns

#### Output:

An excel file with the similar names and the mismatched names in separate columns

### Learning Points:

1. First, consider pre-filtering steps to decrease the candidate pool for the string comparison algorithms to improve overall efficiency.
2. Further optimise reduction of the candidate pool by considering possible post-algorithm manipulations. In this case, considering if there could be similar names within the same list, where one name could be a substring of another within the same list.

## References

1. https://yassineelkhal.medium.com/the-complete-guide-to-string-similarity-algorithms-1290ad07c6b7
2. https://www.geeksforgeeks.org/python-test-if-string-is-subset-of-another/
