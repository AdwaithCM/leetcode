class Solution(object):
    def averageValue(self, nums):
        sum=0
        count=0
        for i in range(0,len(nums)):
            if nums[i] % 2==0 and nums[i] % 3==0:
                sum= sum+nums[i]
                count=count+1
        if count!=0:
            sum=sum/count
            return sum
        else:
            return 0
        