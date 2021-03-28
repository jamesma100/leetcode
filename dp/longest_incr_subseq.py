def lengthOfLIS(nums):
    dp = [1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j]+1, dp[i])
    return max(dp)

def main():
    if lengthOfLIS([1,2,3,3,7]) != 4:
        print("test1 failed")
    if lengthOfLIS([10,9,2,5,3,7,101,18]) != 4:
        print("test2 failed")
    if lengthOfLIS([1,7,4,2,4,10,1,8]) != 4:
        print("test3 failed")
    if lengthOfLIS([0,1,0,3,2,3]) != 4:
        print("test4 failed")
    if lengthOfLIS([7,7,7,7,7,7,7]) != 1:
        print("test5 failed")

if __name__ == '__main__':
    main()