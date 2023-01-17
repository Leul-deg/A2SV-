class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {heights[idx] : names[idx] for idx in range(len(names))}
        store =  [0] * (max(heights) + 1)
        sorted_heights = []
        for height in heights:
            store[height] += 1
        for idx in range(len(store)):
            sorted_heights.extend([idx]*store[idx])
        heights = sorted_heights[-1::-1]
        
        return [hashmap[height] for height in heights]
