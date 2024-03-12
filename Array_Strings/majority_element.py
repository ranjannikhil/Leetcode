class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums) // 2 
       
        print(nums)
        for i in nums:
            c= nums.count(i)
            if c>n:
                k=i
                break
        return k
