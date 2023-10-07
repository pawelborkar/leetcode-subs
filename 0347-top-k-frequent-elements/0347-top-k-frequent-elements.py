class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Since we're given the range of k in the form of [1, no. of unique elements] then don't have to check for nullables of k 

        count = collections.Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)