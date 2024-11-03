class Solution:

    #Brute Force: using two loops
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        
    
    #Better Approach: using hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], index] 
            hashMap[num] = index
        return []







