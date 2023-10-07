class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq = [[] for i in range(len(nums) + 1)]  

        # Count the elements
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        res = []        
        for i in range(len(freq) -1, 0, -1):
            if freq[i] is not None:
                for n in freq[i]:
                    res.append(n)
                    if len(res) == k:
                        return res


