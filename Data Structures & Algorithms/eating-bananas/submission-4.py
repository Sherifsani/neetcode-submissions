class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        upper = max(piles)
        min_k = upper
        lower = 1
        while lower <= upper:
            k = (upper + lower) // 2
            total = 0
            for p in piles:
                total += (p + k - 1) // k
            if total > h:
                lower = k + 1
            else:
                upper = k - 1
                min_k = min(min_k, k)
        return min_k

