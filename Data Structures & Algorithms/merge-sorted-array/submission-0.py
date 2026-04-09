# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         result = []
#         l1 = 0
#         l2 = 1

#         long = nums2 if len(nums2) > len(nums1) else nums1

#         for i in range(len(long)):
#             if l1 < len(nums1) 


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m1, n1, last = m-1, n-1, m+n-1
        
        while n1>=0:
            if m1>=0 and nums1[m1] > nums2[n1]:
                nums1[last] = nums1[m1]
                m1 -= 1
            else:
                nums1[last] = nums2[n1]
                n1 -= 1
            
            last -= 1