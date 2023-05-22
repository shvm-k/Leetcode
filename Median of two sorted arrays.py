class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        merged.extend(nums1[p1:])
        merged.extend(nums2[p2:])

        length = len(merged)
        if length % 2 == 0:
            median = (merged[length // 2 - 1] + merged[length // 2]) / 2
        else:
            median = merged[length // 2]

        return median
