class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i, x in enumerate(nums):
        #     tmp = target - x
        #     if tmp in nums:
        #         j = nums.index(tmp)
        #         break
        # return [i, j]
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        