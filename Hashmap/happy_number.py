class Solution:
    def isHappy(self, n: int) -> bool:
        map=[]
        sum=0
        while(sum!=1):
            sum=0
            while(n!=0):
                rem=n%10
                sum=sum+rem*rem
                n=int(n/10)
            if sum in map:
                return False
            map.append(sum)
            n=sum
        return True
