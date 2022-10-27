func runningSum(nums []int) []int {
    var output = nums
    output[0] = nums[0]
    for i:=1; i<len(nums); i++{
        output[i] = nums[i] + nums[i-1]
    }
    return output
}