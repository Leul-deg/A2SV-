class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0] + list(accumulate(nums))
        q = deque()
        q.append(0)
        res = float('inf')
        for idx , num in enumerate(prefix):

            while q and  num - prefix[q[0]] >= k:
                # q.popleft()
                # if prefix[q[0]]:
                #     res = min(res , idx - q.popleft() + 1)
                # else:
                    res = min(res , idx - q.popleft())

            while q and num <= prefix[q[-1]]:
                q.pop()
            
            q.append(idx)
        
        return res if res != float('inf') else -1