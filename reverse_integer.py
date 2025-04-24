class Solution(object):
    def reverse(self, x):

        r = str(x)[::-1]
        if r[-1] == '-':
            r = '-' + r[:-1]
        if int(r) <= -2**31 or int(r) >= 2**31 - 1:
            return 0
        return int(r)
        