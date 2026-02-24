# CHECK IF TWO RECTANGLES OVERLAP EACH OTHER OR NOT.

*Given two rectangles, find if the given two rectangles overlap or not.
Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates.*

**L1: Top Left coordinate of first rectangle.
<br>
R1: Bottom Right coordinate of first rectangle. 
<br>
L2: Top Left coordinate of second rectangle. 
<br>
R2: Bottom Right coordinate of second rectangle.**

Examples:

```
Input: l1 = { 0, 10 }, r1 = { 10, 0 }, l2 = { 5, 5 }, r2 = { 15, 0 }
Output: Rectangles Overlap

Input: l1 = { 0, 10 }, r1 = { 10, 0 }, l2 = { -10, 5 }, r2 = { -1, 0 }
Output: Rectangles Don't Overlap