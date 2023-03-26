## Digital Root

###

The digital_root function takes an integer n and calculates its digital root by summing the digits of n until the result is a single-digit number. It does this recursively until the sum is less than 10.

Improvement points:

1. The code can be made more efficient by using a while loop instead of a recursive function, which can cause stack overflow errors for very large input numbers.
###
2. The code can be made more readable by using a generator expression instead of a list comprehension to convert the input number into a list of its digits

***Analysis by Matthias and Ott***
