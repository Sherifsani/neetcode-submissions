class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == s2:
            return True

        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord('a')] += 1

        window_freq = [0] * 26
        for c in s2[:len(s1)]:
            window_freq[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if freq == window_freq:
                return True
            window_freq[ord(s2[r]) - ord('a')] += 1
            window_freq[ord(s2[l]) - ord('a')] -= 1
            l += 1
        if freq == window_freq:
            return True

        return False

