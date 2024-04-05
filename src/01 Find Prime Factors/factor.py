def get_prime_factors(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors
    
def prime_factors(n):
    factors = []
    # Check for even factors (2 is the only even prime)
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd factors starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
    number = 60
    print(f"Prime factors of {number}: {prime_factors(number)}")
