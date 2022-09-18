class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict1= {}
        maxSet = []
        output = float('inf')
        for ele in nums:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
        dict1 = sorted(dict1.items(), key = lambda x: x[1], reverse = True)
        maximum = dict1[0][1]
        for ele in dict1:
            if ele[1] == maximum:
                maxSet.append(ele[0])
        maxSet = set(maxSet)
        print(maxSet)
        for ele in maxSet:
            left = 0
            right = len(nums) - 1
            while(left <= right):
                if nums[left] == ele and nums[right] == ele:
                    break
                elif nums[left] != ele:
                    left = left + 1
                elif nums[right] != ele:
                    right = right - 1

            print(left, right)
            output = min(output, (right - left + 1))
        return output
                    
                
        