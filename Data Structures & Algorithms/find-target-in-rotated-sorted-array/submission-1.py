class Solution:
    def search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1

        # check if not rotated
        if nums[l] < nums[r]:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        if target > nums[-1]:
            r = l - 1
            l = 0
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1
        elif target <= nums[-1]:
            r = len(nums) - 1
            print(l , r)
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1
