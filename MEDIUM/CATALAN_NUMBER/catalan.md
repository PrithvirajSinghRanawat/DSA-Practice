# PROGRAM FOR nth CATALAN NUMBER.

*Catalan numbers are defined as a mathematical sequence that consists of positive integers, which can be used to find the number of possibilities of various combinations.  The nth term in the sequence denoted C<sub>n</sub>.*

*The first few Catalan numbers for n = 0, 1, 2, 3, 4, 5… are: 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...  so on.*


**Catalan numbers occur in many interesting counting problems like the following.**

Count the number of expressions containing n pairs of parentheses that are correctly matched.
Count the number of possible Binary Search Trees with n keys (See this)
Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.

Examples:

```
Input: n = 6
Output: 132
Explanation: C(6)=C(0)C(5)+C(1)C(4)+C(2)C(3)+C(3)C(2)+C(4)C(1)+C(5)C(0)=132

Input: n = 8
Output: 1430
Explanation: C(8)=C(0)C(7)+C(1)C(6)+C(2)C(5)+C(3)C(4)+C(4)C(3)+C(5)C(2)+C(6)C(1)+C(7)C(0)=1430

Input: n = 5
Output: 42
Explanation: C(5)=C(0)C(4)+C(1)C(3)+C(2)C(2)+C(3)C(1)+C(4)C(0)=42