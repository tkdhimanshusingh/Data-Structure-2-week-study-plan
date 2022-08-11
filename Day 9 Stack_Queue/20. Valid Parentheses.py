class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if stack and char in parentheses and stack[-1] == parentheses[char]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0