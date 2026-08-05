class Solution:
    def calPoints(self, operations: List[str]) -> int:
        d = "D"
        c = "C"
        sum_of_two = "+" 
        ops = [d,c,sum_of_two]

        stack = []
        last_index = 0
        for i, op in enumerate(operations):
            print(stack)
            print(last_index)
            if op in ops:
                if op == sum_of_two:
                    tmp = stack[last_index-1] + stack[last_index-2]
                    stack.append(tmp)
                    last_index += 1
                elif op == d:
                    tmp = stack[last_index-1] + stack[last_index-1]
                    stack.append(tmp)
                    last_index += 1
                elif op == c:
                    stack.pop()
                    last_index -= 1
            else:
                stack.append(int(op))
                last_index += 1
        return sum(stack)