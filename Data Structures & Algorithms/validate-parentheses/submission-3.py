class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        entry = {'(' : ')', '{': '}', '[': ']'}
        for ch in s:
            if ch in entry:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if ch != entry[popped]:
                    return False
        
        return len(stack) == 0