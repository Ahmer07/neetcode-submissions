class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits 
        number = ""
        for digit in digits:
            number += str(digit)
        number = str(int(number) + 1)
        digits = []
        for num in number:
            digits.append(num)
        return digits
        