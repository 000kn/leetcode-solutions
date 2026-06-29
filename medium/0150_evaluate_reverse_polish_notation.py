# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Difficulty: Medium
# Pattern: Stack — push numbers, pop two on operator, apply in correct order — O(n)

class Solution:
    def evalRPN(self, tokens):
        self.stack = []
        for c in tokens:
            if c in "+-*/":
                num1 = self.stack.pop()
                num2 = self.stack.pop()
                if c == "+":
                    self.stack.append(num2 + num1)
                elif c == "-":
                    self.stack.append(num2 - num1)
                elif c == "*":
                    self.stack.append(num2 * num1)
                elif c == "/":
                    self.stack.append(int(num2 / num1))
            else:
                self.stack.append(int(c))
        return self.stack[0]