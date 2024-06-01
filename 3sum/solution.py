from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # presence_dict: dict[int, int] = {}
        # pair_dict: dict[tuple[int, int], int] = {}
        #
        # for i in range(len(nums)):
        #     if presence_dict[i] is None:
        #         presence_dict[i] = 1
        #     else:
        #         presence_dict[i] += 1
        #
        #     for j in range(i + 1, len(nums)):
        #         pair_dict[(min(nums[i], nums[j]), max(nums[i], nums[j]))] = nums[i] + nums[j]

        presence_dict: dict[[int, int, int], bool] = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        presence_dict[tuple(sorted([nums[i], nums[j], nums[k]]))] = True


        return presence_dict.keys()