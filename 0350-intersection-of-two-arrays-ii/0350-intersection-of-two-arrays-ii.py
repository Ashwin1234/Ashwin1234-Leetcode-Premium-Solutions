class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        output = []
        for ele in nums1:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
        
        for ele in nums2:
            if ele in dict2:
                dict2[ele] = dict2[ele] + 1
            else:
                dict2[ele] = 1
        
        for ele in nums2:
            if ele in dict1:
                if dict1[ele] > 0:
                    for j in range(0, min(dict1[ele], dict2[ele])):
                        output.append(ele)
                        dict1[ele] = 0
        
        return output