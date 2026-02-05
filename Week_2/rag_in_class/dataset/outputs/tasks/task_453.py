import math

def sumofFactors(n):
    if n % 2 != 0:
        return 0
    res = 1
    temp_n = n
    for i in range(2, int(math.sqrt(temp_n)) + 1):
        count = 0
        curr_sum = 1
        curr_term = 1
        while temp_n % i == 0:
            count += 1
            temp_n = temp_n // i
            if i == 2 and count == 1:
                curr_sum = 0
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if temp_n >= 2:
        res *= (1 + temp_n)
    return res
