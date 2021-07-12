class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        wall = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[wall] = nums[i]
                wall += 1
        
        return wall