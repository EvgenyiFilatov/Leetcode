"""
4. Median of Two Sorted Arrays,
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""


class Solution:

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    left_max = nums2[j-1]
                elif j == 0:
                    left_max = nums1[i-1]
                else:
                    left_max = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 0:
                    if i == m:
                        right_min = nums2[j]
                    elif j == n:
                        right_min = nums1[i]
                    else:
                        right_min = min(nums1[i], nums2[j])
                    return (left_max + right_min) / 2.0
                return left_max


find = Solution()
nums1 = [1, 3]
nums2 = [2]
print(find.findMedianSortedArrays(nums1, nums2))
