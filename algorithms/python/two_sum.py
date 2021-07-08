class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        index_of = dict()
        for i in range(len(nums)):
            this = nums[i]
            diff = target - this
            if diff in seen:
                return [index_of[diff], i]
            else:
                seen.add(this)
                index_of[this] = i