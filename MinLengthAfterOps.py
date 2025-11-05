class Solution:
    def minimumLength(self, s: str) -> int:
        
        mp = {}
        for i in s:
            mp[i] = mp.get(i, 0) + 1
    
        for i in range(len(s)):
            if mp[s[i]] < 3:
                continue
            
            mp[s[i]] -= 2

        #print(mp)
        return sum(mp.values())
