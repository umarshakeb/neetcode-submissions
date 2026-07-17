class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_list = [[] for _ in range(len(nums)+1)]
        count = {}
        for i in range(len(nums)):
            if nums[i] in count.keys():
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        for num, freq in count.items():
            bucket_list[freq].append(num)
        res = []
        for freq in range(len(bucket_list)-1, 0, -1):
            for num in bucket_list[freq]:
                print(num)
                res.append(num)
                if len(res)==k:
                    return res

        