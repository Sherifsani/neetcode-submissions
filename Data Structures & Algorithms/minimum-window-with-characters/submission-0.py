class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == s: 
            return t

        t_map = dict()
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
    
        l = 0
        need = len(set(t))
        window = dict()
        res = ""
        
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            
            if s[r] in t_map and window[s[r]] == t_map[s[r]]:
                need -= 1
                
            # The while loop needs to be at the for-loop level,
            # not nested inside the if statement above.
            while need == 0:
                if len(res) == 0 or (r - l + 1) < len(res):
                    res = s[l:r+1]
                    
                window[s[l]] -= 1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    need += 1
                l += 1
                
        return res

