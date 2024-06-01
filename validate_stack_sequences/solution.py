from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack_simulation: list[int] = []

        push_pointer: int = 0
        pop_pointer: int = 0

        while pop_pointer != len(pushed) or push_pointer != len(popped):
            if pop_pointer != len(popped) and len(stack_simulation) != 0 and popped[pop_pointer] == stack_simulation[-1]:
                stack_simulation.pop(-1)
                pop_pointer += 1
                continue

            if push_pointer != len(pushed):
                stack_simulation.append(pushed[push_pointer])
                push_pointer += 1
                continue

            return False
        
        return True
                

if __name__ == "__main__":
    test1 = [1,2,3,4,5]
    test2 = [4,3,5,1,2]

    print(Solution().validateStackSequences(test1, test2))
