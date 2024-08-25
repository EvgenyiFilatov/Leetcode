class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False


palindrom = Solution()
x = 121
print(palindrom.isPalindrome(x))
