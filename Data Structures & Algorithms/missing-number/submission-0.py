class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = range(0, len(nums)+1)
        for num in all_nums:
            if num not in nums:
                return num
        