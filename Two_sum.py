def twoSum(self, nums: List[int], target: int) -> List[int]:

        # i and j loop through each elemtent to find the target sum
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j