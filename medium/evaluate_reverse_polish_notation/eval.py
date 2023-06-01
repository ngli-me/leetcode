from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = tokens.pop(len(tokens) - 1)

        if op.lstrip('-').isnumeric():
            return int(op)
        pos_2 = int(tokens.pop(len(tokens) - 1)) \
                if tokens[len(tokens) - 1].lstrip('-').isnumeric() \
                else self.evalRPN(tokens)
        pos_1 = int(tokens.pop(len(tokens) - 1)) \
                if tokens[len(tokens) - 1].lstrip('-').isnumeric()  \
                else self.evalRPN(tokens)
        match op:
            case '+':
                return int(pos_1 + pos_2)
            case '-':
                return int(pos_1 - pos_2)
            case '*':
                return int(pos_1 * pos_2)
            case '/':
                return int(pos_1 / pos_2)
            case _:
                return 0

def main():
    s = Solution()
    # print(s.evalRPN(["4","13","5","/","+"]))
    # print(s.evalRPN(["2","1","+","3","*"]))
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))




if __name__ == "__main__":
    main()
