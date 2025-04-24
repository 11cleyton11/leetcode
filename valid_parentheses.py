class Solution(object):
    def isValid(self, s):

        map = {')':'(',
               ']':'[',
               '}':'{'}
        openers = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                openers.append(char)
            else:
                if not openers:
                    return False
                elif map[char] == openers[-1]:
                    openers.pop()
                else:
                    return False
        if not openers:
            return True

        return False