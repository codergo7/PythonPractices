number = int(input("Eneter a number please: "))
def isPrime(n):
    flag = True
    for i in range(2, n):
        if (n % i == 0):
            flag = False
        i += 1
    return flag


def find_prime_numbers(n):
    primes = []
    for i in range(2, n):
        b = isPrime(i)
        if b == True:
            primes.append(i)
    return primes

print(find_prime_numbers(number))