class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for x in nums:
            if x not in mp:
                mp[x]=0
            mp[x]+=1
        sorted_mp = dict(sorted(mp.items(),key=lambda x:x[1],reverse=True))
        return list(sorted_mp.keys())[:k]
