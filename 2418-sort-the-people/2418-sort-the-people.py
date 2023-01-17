class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {heights[idx] : names[idx] for idx in range(len(names))}
        # def bubble_sort(array):
        #     for i in range(len(array)):
        #         for j in range(len(array)):
        #             if j+1 < len(array) and array[j] < array[j+1]:
        #                 array[j] , array[j+1] = array[j+1] , array[j]
        # bubble_sort(heights)
        def selection_sort(array):
            def min_index(arr):
                cur_min = arr[0]
                min_idx = 0
                for idx in range(len(arr)):
                    if cur_min > arr[idx]:
                        min_idx = idx
                        cur_min = arr[idx]
                return min_idx
            for i in range(len(array)):
                min_idx = min_index(array[:len(array) - i])
                array[min_idx] , array[len(array) - 1 - i] = array[len(array) - 1 - i]  , array[min_idx]
        
        selection_sort(heights)
        return [hashmap[height] for height in heights]
