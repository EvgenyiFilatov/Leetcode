"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list = []
        for i in s:
            if i in '({[':
                stack.append(i)
            elif i in ')}]':
                if len(stack) == 0:
                    return False
                top_element = stack.pop()
                if i == ')' and top_element == '(':
                    continue
                if i == '}' and top_element == '{':
                    continue
                if i == ']' and top_element == '[':
                    continue
                else:
                    return False
        return True if not stack else False

    def isValidDict(self, s: str) -> bool:
        brackets_dict = {')': '(', '}': '{', ']': '['}
        stack: list = []
        for char in s:
            if char in brackets_dict:
                top_element = stack.pop() if stack else False
                if brackets_dict[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


valid = Solution()
s = "(]"
print(valid.isValid(s))
print(valid.isValidDict(s))
