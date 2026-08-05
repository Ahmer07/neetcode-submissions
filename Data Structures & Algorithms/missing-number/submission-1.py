class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # all_nums = range(0, len(nums)+1)
        # for num in all_nums:
        #     if num not in nums:
        #         return num

        max_num = len(nums) + 1
        current_num = 0
        while current_num <= max_num:
            if current_num not in nums:
                return current_num
            current_num += 1
        