class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = collections.defaultdict(int)

        for i, num in enumerate(nums):

            counter[num] = 1 + counter.get(num, 0)

            if counter.get(num) > 1:
                return True
        
        return False

       

        