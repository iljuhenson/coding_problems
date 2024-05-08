class Solution:
    def intToRoman(self, num: int) -> str:
        all_letters = ["IVX", "XLC", "CDM", "MMM"]
        ans = ""
        idx = 0
        while num != 0:
            ans = self.helper(num % 10, all_letters[idx]) + ans
            num //= 10
            idx += 1

        return ans


    def helper(self, number: int, letters: str) -> str:
        match number:
            case 0:
                return ""
            case 1:
                return letters[0]
            case 2:
                return letters[0] + letters[0]
            case 3:
                return letters[0] + letters[0] + letters[0]
            case 4:
                return letters[0] + letters[1]
            case 5:
                return letters[1]
            case 6:
                return letters[1] + letters[0]
            case 7:
                return letters[1] + letters[0] + letters[0]
            case 8:
                return letters[1] + letters[0] + letters[0] + letters[0]
            case 9:
                return letters[0] + letters[2]
