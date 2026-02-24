# PROGRAM TO FIND THE DIGITAL ROOT OF ANY NUMBER.

*The digital root of a positive integer is found by summing the digits of the integer. If the resulting value is a single digit then that digit is the digital root. If the resulting value contains two or more digits, those digits are summed and the process is repeated. This is continued as long as necessary to obtain a single digit.*

**Given a number, the task is to find its digital root. The input number may be large and it may not be possible to store even if we use long long int.**

Examples :

```
Input : num = "1234"
Output : 1
Explanation : The sum of 1+2+3+4 = 10, digSum(x) == 10,Hence ans will be 1+0 = 1

Input : num = "5674"
Output : 4