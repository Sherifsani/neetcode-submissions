class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        sorted_piles = list(sorted(piles))
        print(sorted_piles)
        upper = sorted_piles[-1]
        min_k = upper
        lower = 1
        while lower <= upper:
            k = (upper + lower) // 2
            total = 0
            for i in piles:
                total += math.ceil(i/k)
            if total > h:
                lower = k + 1
            else:
                upper = k - 1
                min_k = min(min_k, k)
        return min_k

