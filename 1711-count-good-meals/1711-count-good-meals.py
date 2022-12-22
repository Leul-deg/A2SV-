class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        counter = Counter(deliciousness)
        res = 0
        for num in counter:
            if num != 0:
                log = math.log(num , 2)
                if int(log) == log:
                    res += counter.get(0,0) * counter.get(num)
                    res += math.comb(counter.get(num) , 2)
                else:
                    ceiling = math.ceil(log)
                    nearest_power= 2**ceiling
                    if nearest_power - num in counter:
                        res += counter.get(nearest_power - num) * counter.get(num)
        return res%MOD

                
                