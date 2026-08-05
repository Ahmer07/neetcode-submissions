class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons_ones = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
                if ones > max_cons_ones:
                    max_cons_ones = ones 
            else:
                ones = 0
        return max_cons_ones
        