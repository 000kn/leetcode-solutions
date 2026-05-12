"""
LeetCode #20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Trick: Stack kullan. Açılan parantezi push, kapanan parantez
geldiğinde pop'tan eşleşme kontrol. Sonda stack boşsa valid.

Time: O(n)
Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))        # True
    print(sol.isValid("()[]{}"))    # True
    print(sol.isValid("(]"))        # False
    print(sol.isValid("([)]"))      # False
    print(sol.isValid("{[]}"))      # True