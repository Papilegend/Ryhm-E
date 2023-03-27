def digital_root(n):
    # Input validation
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer."
    
    # Base case
    if n < 10:
        return n
    
    # Recursive case
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digital_root(digit_sum)
        
print(digital_root(15)) # 6
print(digital_root(942)) # 6
print(digital_root(132189)) # 6
print(digital_root(493193)) # 2
print(digital_root(30142200412699912)) # 3
print(digital_root(-10)) # Error: Input must be a positive integer.
print(digital_root("abc")) # Error: Input must be a positive integer.
