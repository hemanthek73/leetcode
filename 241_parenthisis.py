class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def evaluate(expression):
            if expression.isdigit():
                return [int(expression)]

            output = []
            for i in range(len(expression)):
                if expression[i] in ["+","-","*"]:
                    leftpart = evaluate(expression[:i])
                    rightpart = evaluate(expression[i+1:])

                    for left in leftpart:
                        for right in rightpart:
                            if expression[i] == '+':
                                output.append(left+right)
                            elif expression[i] == '-':
                                output.append(left-right)
                            elif expression[i] == '*':
                                output.append(left*right)        
            return output
        return evaluate(expression)   

        