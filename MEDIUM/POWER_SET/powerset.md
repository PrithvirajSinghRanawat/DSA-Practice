# PROGRAM TO FIND THE POWER SET.

*Power Set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}. If S has n elements in it then P(s) will have 2n elements.*

Examples :

```
Input: s = "ab"
Output: "", "a", "b", "ab"
Explanation: The power set of "ab" includes all possible subsets: empty set, single characters, and full string.

Input: s = "abc"
Output: "", "a", "b", "c", "ab", "bc", "ac", "abc"
Explanation: The power set of "abc" includes all subsets formed by choosing any combination of its characters.

Input: s = "a"
Output: "", "a"
Explanation: The power set of "a" consists of the empty set and the single character itself.