class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low = 0
        high = rows - 1
        while low <= high:
            mid = (low+high)//2
            if target > matrix[mid][-1]:
                low = mid+1
            elif target < matrix[mid][0]:
                high = mid -1
            else:
                row = mid
                break
        else:
            return False

        left, right = 0, len(matrix[mid]) -1
        while left<= right:
            mid = (left+right)//2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False



