class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums1 = list()
        for i in range(len(nums)):
            if nums[i] in nums1:
                nums1.remove(nums[i])
            else:
                nums1.append(nums[i])
        return nums1[0]
            
            