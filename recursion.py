def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)# recursive call
result = factorial(7)
print(result)
#"Since n == 1 is the base case, when n = 1 is reached, it returns 1 without executing the print statement; however, the function begins the calculation after 'unwinding' and starts printing the results before the base case (i.e., when n == 1, return 1), such as in factorial(2)."


