class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(left,right):
            if left>right:
                return -1
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binary_search(left,mid-1)
            else:
                return binary_search(mid+1,right)
        return binary_search(0, len(nums)-1)