class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            wall = 0
            for i in range(1, len(nums)):
                if nums[i] != nums[wall]:
                    wall += 1
                    nums[wall] = nums[i]
            return wall + 1