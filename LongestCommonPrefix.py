class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        maxlen = min(len(s) for s in strs)
        current = ""

        for r in range(maxlen):
            charcheck = strs[0][r]
            if all(s[r] == charcheck for s in strs):
                current += charcheck
            else:
                break

        return current
