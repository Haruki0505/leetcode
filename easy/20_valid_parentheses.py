class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif stack != [] and stack[-1] == hashmap[char]:
                stack.pop()
            else:
                return False

        return stack == []

obj = Solution()
print(obj.isValid("([]1)"))