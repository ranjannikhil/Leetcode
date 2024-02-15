class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map={}
        for i,n in enumerate(nums):
            if n in map:
                diff=i-map[n]
                if diff<=k:
                    return True
                else:
                    map.update({n:i})
            else:
                map[n]=i
        return False
