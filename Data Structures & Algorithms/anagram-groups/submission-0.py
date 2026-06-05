class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            hashmap = [0] * 26
            for c in s:
                hashmap[ord(c)-ord("a")] +=1
            result[tuple(hashmap)].append(s)
        return list(result.values())