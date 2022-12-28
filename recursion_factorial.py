def nfact(n):
    if n < 0:
        raise ValueError("Negative numbers is not a valid input for nfact.")
    fact = 0
    if n == 1 or n == 0:  # base cases
        fact = 1
    else:
        fact = n * nfact(n - 1)

    return fact
