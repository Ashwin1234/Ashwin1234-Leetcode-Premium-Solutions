class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        output = []
        for ele in nums1Set:
            if ele in nums2Set:
                output.append(ele)
        return output
        