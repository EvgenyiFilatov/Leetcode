class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index: dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []


find_two_nums = Solution()
nums = [2, 5, 5, 11]
target = 10
print(find_two_nums.twoSum(nums, target))
