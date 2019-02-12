def isPrime(n_str):
    n = int(n_str)
    if(n<2):
        return False;
    factors = []
    is_prime = True
    for i in range(2, n):
        if n%i == 0:
            is_prime = False
            factors.append(i)
    return is_prime, factors
