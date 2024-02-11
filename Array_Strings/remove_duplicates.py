class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=None
        j=0
        for i in range(len(nums)):
            if nums[i]!=prev:
                nums[j]=nums[i]
                prev=nums[i]
                j+=1
        return j
            
