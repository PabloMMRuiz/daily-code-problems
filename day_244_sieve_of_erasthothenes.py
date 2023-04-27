"""The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
The method is to take increasingly larger prime numbers, and mark their multiples as composite.
For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] 
(multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.
Implement this algorithm.
Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input)."""


def sieve_of_eratosthenes(ceiling: int)->list:
    cicle = 2
    temp = 2
    nums = [True for _ in range(ceiling+1)]
    primes = [0, 1]
    for index, prime in enumerate(nums):
        if index == 0 or index == 1:
            continue
        elif prime:
            primes.append(index)
            while temp*index < len(nums):
                nums[temp*index] = False
                temp +=1
            temp=2
    return primes
print(sieve_of_eratosthenes(1000))


