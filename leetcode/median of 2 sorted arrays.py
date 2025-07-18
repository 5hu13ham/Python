"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
##easy method - time taking##########################
        nums3 = sorted(nums1 + nums2)
        print (nums3)
        print (len(nums3) / 2)
        if len(nums3) % 2 == 0:
            return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2
        else:
            return nums3[len(nums3)//2]

## faster way########################################

        nums4 = nums1 + nums2
        


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(result)