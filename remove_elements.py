"""https://leetcode.com/problems/remove-element/description/"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


remove = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(remove.removeElement(nums, val))
