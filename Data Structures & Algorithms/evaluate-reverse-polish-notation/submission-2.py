class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = {"+","-","*","/"}

        for x in tokens:
            
            if x not in operators:
                nums.append(int(x))
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                if x == "+": nums.append(num1 + num2)
                if x == "-": nums.append(num1 - num2)
                if x == "*": nums.append(num1 * num2)
                if x == "/": nums.append(int(num1 / num2))
        
        return nums.pop()