from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1

        while True:
            middle_idx = (right_idx + left_idx) // 2
            
            # print(f"left and right: ${left_idx} ${right_idx}")

            if nums[middle_idx] == target:
                return middle_idx
            elif middle_idx == left_idx and middle_idx == right_idx:
                return -1
            elif target > nums[right_idx] and target < nums[left_idx]:
                return -1

            if nums[middle_idx] >= nums[left_idx] and nums[middle_idx] >= nums[right_idx] and nums[left_idx] >= nums[right_idx]:
                if target >= nums[left_idx] and target <= nums[middle_idx]:
                    right_idx = middle_idx - 1
                    continue
                else:
                    left_idx = middle_idx + 1
                    continue

            if nums[middle_idx] <= nums[left_idx] and nums[middle_idx] <= nums[right_idx] and nums[left_idx] >= nums[right_idx]:
                if target >= nums[middle_idx] and target <= nums[right_idx]:
                    left_idx = middle_idx + 1
                    continue
                else:
                    right_idx = middle_idx - 1
                    continue

            if nums[middle_idx] >= nums[left_idx] and nums[middle_idx] <= nums[right_idx] and nums[left_idx] <= nums[right_idx]:
                if target > nums[right_idx] or target < nums[left_idx]:
                    return -1

                if target <= nums[middle_idx]:
                    right_idx = middle_idx - 1
                    continue
                elif target >= nums[middle_idx]:
                    left_idx = middle_idx + 1
                    continue

if __name__ == "__main__":
    test_arr = [4,5,6,7,0,1,2]
    test_target = 0

    print(Solution().search(test_arr, test_target))
