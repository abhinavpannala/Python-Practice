class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        location = {}
        list1 = []
        for i in range(len(nums)):
            if target-nums[i] in location.keys():
                list1 = [location[target-nums[i]],i]
                break
            else:
                location[nums[i]] = i
        return list1