from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_counter: dict = {}

        for num in nums:
            if num in num_counter:
                num_counter[num] += 1
            else:
                num_counter[num] = 1

        operations: int = 0
        for num, repetitions in num_counter.items():
            current_num_operations: int = repetitions // 3
            remainder: int = repetitions % 3

            if (remainder == 1 and current_num_operations != 0) or (remainder == 2):
                current_num_operations += 1
            elif remainder != 0:
                return -1
            
            operations += current_num_operations
        
        return operations


if "__main__" == __name__:
    test_case = [2,3,3,2,2,4,2,3,4]

    print(Solution().minOperations(test_case))