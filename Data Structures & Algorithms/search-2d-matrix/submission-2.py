class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row = None
        
        #do binary search on the rows in general to find which row to look through
        leftRow, rightRow = 0, rows - 1
        while leftRow <= rightRow:
            midRow = (leftRow + rightRow) // 2
            if matrix[midRow][0] <= target and target <= matrix[midRow][-1]:
                row = midRow
                break
            elif target > matrix[midRow][-1]:
                leftRow = midRow + 1
            elif target < matrix[midRow][0]:
                rightRow = midRow - 1
        
        leftVal, rightVal = 0, cols - 1
        while row != None and leftVal <= rightVal:
            midVal = (leftVal + rightVal) // 2
            if matrix[row][midVal] == target:
                return True
            elif matrix[row][midVal] < target:
                leftVal = midVal + 1
            else:
                rightVal = midVal - 1
        
        return False
