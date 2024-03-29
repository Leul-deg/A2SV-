class Solution:
    def calculate(self, s: str) -> int:
        index = 0
        stack = []
        exp = False
        while index < len(s):
            char = s[index]
            if char == " ":
                index+=1
                continue
            elif char in "+-/*":
                if char in "*/":
                    stack.append(char)
                    index+=1
                    exp = True
                    continue
                else:
                    stack.append(char)
                    index+=1
            else:
                num = ""
                while index<len(s) and s[index] not in "+-*/ ":
                    num+=s[index]
                    index+=1
                
                stack.append(int(num))
            
            if exp:
                num2 = stack.pop()
                expression = stack.pop()
                num1 = stack.pop()
                if expression == "*":
                    stack.append(num1*num2)
                else:
                    res = num1/num2
                    stack.append(int(res))
                exp = False
                    
                
        stack2  = []
        exp = False
        for index,char in enumerate(stack):
            if str(char) in "+-":
                exp = True
                stack2.append(char)
                
            elif exp:
                num2 = char
                expression = stack2.pop()
                num1 = stack2.pop()
                if expression =="+":
                    stack2.append(num1 + num2)
                else:
                    stack2.append(num1 - num2)
                exp = False
            else:
                stack2.append(char)
            
        return stack2[0]