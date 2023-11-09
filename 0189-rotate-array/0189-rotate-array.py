class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if len(nums)==1:
            return
        nums[:]= nums[len(nums)-k:]+nums[:len(nums)-k]

        #nums[:]=[nums[(i+k+1)%len(nums)] for i in range(len(nums))]
        