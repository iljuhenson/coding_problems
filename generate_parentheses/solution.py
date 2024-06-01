from typing import List

class Solution:
    def __init__(self):
        self.answer: set[str] = set(["()",])

    def generate_paranthesis_combinations(self, paranthesis_string: str) -> None:
        for i in range(len(paranthesis_string)):
            self.answer.add(paranthesis_string[:i] + "()" + paranthesis_string[i:])

    def generateParenthesis(self, n: int) -> List[str]:
        for _ in range(1, n):
            extracted_set: set[str] = self.answer
            self.answer = set()

            for current_paranthesis_string in extracted_set:
                self.generate_paranthesis_combinations(current_paranthesis_string)


        return list(self.answer)
    

if __name__ == "__main__":
    test_case = 3

    print(Solution().generateParenthesis(test_case))