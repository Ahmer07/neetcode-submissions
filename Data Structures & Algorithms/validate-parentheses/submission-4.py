class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            print(stack)
            if i in mapping.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == mapping[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if stack != []:
            return False
        return True
