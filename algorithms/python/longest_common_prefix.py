class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''
        shortest_length = min(len(s) for s in strs)
        res = []
        for i in range(shortest_length):
            _set = set(s[i] for s in strs)
            if len(_set) > 1:
                return ''.join(res)
            else:
                res.append(strs[0][i])
        return ''.join(res)