class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        if sum(nums)%2!=0:
            return False
        print(target)
        for i in range(len(nums) -1 , -1, -1):
            dp1 = set()
            for ele in dp:
                dp1.add(ele)
                dp1.add(ele + nums[i])
            dp = dp1
        if target in dp:
            return True
        else:
            return False