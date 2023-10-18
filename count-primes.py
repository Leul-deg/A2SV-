class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2 : return 0
        is_prime = [True] * (n + 1)

        primes = 0 
        is_prime[0] = False
        is_prime[1] = False 
        for idx in range(2 , len(is_prime) ):

            mult = idx
            cur = False 
            while is_prime[idx] and idx * mult < len(is_prime):
                is_prime[idx * mult] = False

                mult += 1
                cur = True
            
            primes += cur
        # print(is_prime)
        is_prime.pop()
        return is_prime.count(True)