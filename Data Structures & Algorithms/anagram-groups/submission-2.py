class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs: 
            s_ = ''.join(sorted(list(s)))
            if s_ in hm.keys():
                hm[s_].append(s)
            else:
                hm[s_] = [s]
        return list(hm.values())
