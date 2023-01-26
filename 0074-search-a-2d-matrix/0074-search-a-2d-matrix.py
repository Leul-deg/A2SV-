class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r  = 0 , len(matrix)-1
        while l <= r:
            mid = (l+r)//2
            length = len(matrix[mid])
            if target>=matrix[mid][0] and target<=matrix[mid][length-1]:
                return self.binarySearch(matrix[mid],target)
            elif target < matrix[mid][0]:
                 r = mid -1
            else:
                l = mid+1
        return False
    def binarySearch(self,array,target):
        l,r = 0 , len(array)-1
        while l <=r:
            mid  = (l+r)//2
            if array[mid]== target:
                return True
            elif target>array[mid]:
                l = mid+1
            else:
                r = mid-1
        return False
                
        