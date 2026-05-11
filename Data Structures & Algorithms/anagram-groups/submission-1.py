class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #我要知道把什么当成key
        groups = {}
        for word in strs:
            #这个要再拆一下
            key = ''.join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())