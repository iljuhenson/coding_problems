class Solution:
    numbers_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        return self.recursionCombinator(digits, "", 0, [])

    def recursionCombinator(self, digits: str, current_combination: str, current_digit_idx: int, combination_list: List[str]) -> List[str]:
        if digits == "":
            return []
        
        if len(digits) == len(current_combination):
            # print(current_combination)
            combination_list.append(current_combination)
            return combination_list
            
        for letter in self.numbers_to_letters[digits[current_digit_idx]]:
            self.recursionCombinator(digits, current_combination + letter, current_digit_idx + 1, combination_list)

        return combination_list
