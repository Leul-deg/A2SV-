from sortedcontainers import SortedList

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        arr = []
        
        for i,n in enumerate(nums):
            arr.append((n,i))
        arr.sort()
        
        def getValid(start,end):
            count = end-start + 1
            return (count+1) // 2
        
        segments = SortedList([[0,len(nums)-1]])
        can_pick_up = getValid(segments[0][0],segments[0][1])
        
        while True:
            num,idx = arr.pop()
            target_idx = segments.bisect_left([idx,float("inf")]) - 1
            
            seg_start,seg_end = segments[target_idx]
            can_pick_up -= getValid(seg_start,seg_end)
            segments.remove([seg_start,seg_end])
            if idx == seg_start and idx == seg_end:
                # no need to insert new segment
                pass
            elif idx == seg_start:
                can_pick_up += getValid(idx+1,seg_end)
                segments.add([idx+1,seg_end])
            elif idx == seg_end:
                can_pick_up += getValid(seg_start,idx-1)
                segments.add([seg_start,idx-1])
            else:
                can_pick_up += getValid(seg_start,idx-1)
                can_pick_up += getValid(idx+1,seg_end)
                segments.add([seg_start,idx-1])
                segments.add([idx+1,seg_end])
            
            if can_pick_up < k:
                return num
                
        return -1
                
            
        