class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=None
        j=0
        for i in range(len(nums)):
            if prev!=nums[i]:
                nums[j]=nums[i]
                j=j+1
                prev=nums[i]

        nums[:] = nums[:j]
