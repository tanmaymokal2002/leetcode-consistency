
class Solution:

    #brute force approach: using two loops
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i]==nums[j]:
                    return True
        return False
    '''

    #better approach: using sorting
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                return True
        return False
    '''

    #optimal approach: using hashset
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False
    '''

    #optimal approach: using hashMap
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num in hashMap and hashMap[num] >= 1:
                return True
            hashMap[num] = hashMap.get(num, 0) + 1
        return False




