class Solution:

    #brute force approach = using sorting:
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted(s)
        str2 = sorted(t)
        if str1==str2:
            return True
        else:
            return False
    '''

    #Approach 1 = using map:
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = {}
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        for char in t:
            if char not in hashMap or hashMap[char] == 0:
                return False
        return True
    '''

    #Approach 2 = using ASCII values:
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        if len(s)!=len(t):
            return False
        for char in s:
            count[ord(char) - ord('a')] += 1
        for char in t:
            if count[ord(char) - ord('a')] == 0:
                return False
            count[ord(char) - ord('a')] -= 1
        return True
    '''

    #Approach 3 = using map:
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        return s_map == t_map
    '''

    #Approach 4 = using sorting:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        return s_sorted == t_sorted


        

    
        
        




        