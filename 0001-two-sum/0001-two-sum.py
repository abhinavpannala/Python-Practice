class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        location = {}
        for i in range(len(nums)):
            if target-nums[i] in location.keys():
                return [location[target-nums[i]],i]
            else:
                location[nums[i]] = i