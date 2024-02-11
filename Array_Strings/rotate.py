class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(k):
          temp=nums[:-1]
          nums[0]=nums[-1]
          nums[1:]=temp
