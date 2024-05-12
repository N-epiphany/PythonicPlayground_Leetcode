class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1
        
        while start_index <= end_index : 
            midpoint = start_index + (end_index - start_index) // 2
            midpoint_value = nums[midpoint]

            if midpoint_value == target:
                return midpoint
            
            elif target > midpoint_value:
                start_index = midpoint + 1
                
            else:
                end_index = midpoint - 1 
                
        return start_index
                
