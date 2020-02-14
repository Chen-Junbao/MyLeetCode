class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        # For case where len1 + len2 is odd: left == right
        # For case where len1 + len2 is even: left == right - 1, calculate mean
        left = (len1 + len2 + 1) // 2
        right = (len1 + len2 + 2) // 2

        return (self.get_kth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, left) + self.get_kth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, right)) / 2

    def get_kth(self, nums1, begin1, end1, nums2, begin2, end2, k):
        len1 = end1 - begin1 + 1
        len2 = end2 - begin2 + 1

        if len1 == 0:
            # nums1 array is empty, so the median is in nums2
            return nums2[begin2 + k - 1]
        if len2 == 0:
            # nums2 array is empty, so the median is in nums1
            return nums1[begin1 + k - 1]
        if k == 1:
            # Find min
            if nums1[begin1] < nums2[begin2]:
                return nums1[begin1]
            else:
                return nums2[begin2]
        # Get k/2 value in nums1 and num2
        if len1 < k // 2:
            # nums1 is not enough
            i = begin1 + len1 - 1
        else:
            i = begin1 + k // 2 - 1
        if len2 < k // 2:
            # nums2 is not enough
            j = begin2 + len2 - 1
        else:
            j = begin2 + k // 2 - 1

        if nums1[i] > nums2[j]:
            # (j - begin2 + 1) numbers in nums2 array are less than nums1[i]
            return self.get_kth(nums1, begin1, end1, nums2, j + 1, end2, k - (j - begin2 + 1))
        else:
            # (i - begin1 + 1) numbers in nums1 array are less than nums2[j]
            return self.get_kth(nums1, i + 1, end1, nums2, begin2, end2, k - (i - begin1 + 1))
