class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {heights[idx] : names[idx] for idx in range(len(names))}
        def bubble_sort(array):
            for i in range(len(array)):
                for j in range(len(array)):
                    if j+1 < len(array) and array[j] < array[j+1]:
                        array[j] , array[j+1] = array[j+1] , array[j]
        bubble_sort(heights)
        return [hashmap[height] for height in heights]
