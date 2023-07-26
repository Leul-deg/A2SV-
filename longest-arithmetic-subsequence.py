class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:


        store = []

        def follow(hashmap , value):

            first = hashmap
            ans = 0
            while value in hashmap:

                next_idx = hashmap[value]

                next_hashmap = store[next_idx]
                # if hashmap != first:
                #     hashmap.pop(value)

                hashmap = next_hashmap

                ans += 1

                # if ans > len(nums):
                #     break

            
            return ans + 1


        for i in range(len(nums)):
            cur  = {}
            # if i == len(nums) - 2:
            #     print("waht the fuckk")
            for j in range(i +1, len(nums)):

                

                diff = nums[j] - nums[i]
                if diff not in cur:
                    cur[diff] = j

            # if i == len(nums) - 2:
            #     print("what the fuckkkkk 2" , cur)
            store.append(cur)
        res = 0
        for i in range(len(nums)):

            for key in store[i]:

                

                res = max(follow(store[i] ,   key) , res)
        
        # print(len(store) == len(nums))
        # print(max(Counter(nums).values()))
        # print(store)
        return res