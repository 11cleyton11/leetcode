class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0

        for i in s:
            total += map[i]

        if 'CD' in s or 'CM' in s:
            total -= 200
        
        if 'XL' in s or 'XC' in s:
            total -= 20
        
        if 'IV' in s or 'IX' in s:
            total -= 2

        return total