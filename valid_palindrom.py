class Solution:
    def isPalindrome(self, s: str) -> bool:
      l,r=0,len(s)-1
      s=s.lower()
      while r>l:
        if self.checkalnum(s[l]) and self.checkalnum(s[r]):
          if s[l] != s[r]:
            return False
          else:
            l=l+1
            r=r-1
        elif s[l].isalnum()==False:
          l=l+1
        elif s[r].isalnum()==False:
          r=r-1
      
      return True

    def checkalnum(self,c):
      return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))



    

s="race a car"
print(len(s)-1)
v = Solution().isPalindrome(s=s)
print(v)