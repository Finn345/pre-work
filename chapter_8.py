def is_prime(num):
    """Naive method of checking for primes"""
    for n in range(2,num):
        if num % n == 0:
            print('not prime')
            break
        else: #If never mod zero, then prime
            print('prime')
is_prime(25)