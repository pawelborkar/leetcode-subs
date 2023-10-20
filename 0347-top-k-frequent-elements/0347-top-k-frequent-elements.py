class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        
        if size == 1:
            return nums
        
        freqArray = [[] for i in range(size + 1)]
        counter = {}
        res = []

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        # Add the occurrence into the freqArray
        for number, count in counter.items():
            freqArray[count].append(number)
        
        for i in range(len(freqArray) - 1, 0, -1):
            # we used 0 because if any number present in the array then the count is atleast one
            for n in freqArray[i]:
                res.append(n)
                if len(res) == k:
                    return res