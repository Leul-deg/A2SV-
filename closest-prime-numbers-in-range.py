class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        #generate prime numbers using sieve algorithm up number n
        # n = int(input("Enter the number: "))    
        prime = [True for i in range(right+1)]
        p = 2
        while (p * p <= right):
            if (prime[p] == True):
                for i in range(p * p, right + 1, p):
                    prime[i] = False
            p += 1

        res = []
        for p in range(2, right + 1):
            if prime[p]:
                res.append(p)
        if len(res) < 2:
            return [-1 , -1]
        idx = bisect_left(res , left)
        l , r = idx  , idx + 1 
        diff = 0 
        # print(res)
        i  ,  j = l , len(res) - 1
        while r < len(res):
            if res[j] - res[i] > res[r] - res[l]:
                i ,j  = l , r 
            l += 1
            r += 1
        # print(res)
        return [res[i] , res[j]] if j < len(res) and i < len(res) and res[i] != res[j] else [-1 , -1]