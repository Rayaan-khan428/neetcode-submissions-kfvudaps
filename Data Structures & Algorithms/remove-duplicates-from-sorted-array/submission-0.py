class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Given array sorted in increasing order

        n = len(nums)

        # init left and right pointer to 0
        l = r = 0

        # while the right pointer is less than the length of the array
        while r < n:

            # set the left pointer = to the right pointer
            nums[l] = nums[r]

            # then while ensuring r < n check if what's at the right pointer
            # equals what is at the left pointer
            while r < n and nums[r] == nums[l]:
                # increase r by 1
                r += 1
            
            # move up left pointer
            l += 1
        return l
 