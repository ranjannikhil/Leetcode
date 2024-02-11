class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=None
        j=0
        for i in range(len(nums)):
            if nums[i]!=prev:
                nums[j]=nums[i]
                prev=nums[i]
                j+=1
                n=i+1
                if n<len(nums) and nums[i]==nums[i+1]:
                  nums[j]=nums[i+1]
                  j=j+1
        nums=nums[:j]  
        print(nums)
        return j
