class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
        return prefix


prefix = Solution()
strs = ["flower", "flow", "flight", 'fg']
print(prefix.longestCommonPrefix(strs))
