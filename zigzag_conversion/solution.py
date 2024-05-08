class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # P   A   H   N
        # A P L S I I G
        # Y   I   R
        
        # PAYPALISHIRING

        if numRows == 1:
            return s
        
        ans = ""

        for i in range(0, len(s), (numRows - 1) * 2):
            ans += s[i]

        for i in range(1, numRows - 1):
            for j in range(i, len(s), (numRows - 1) * 2):
                additional_idx = j + (numRows - 1 - i) * 2
                if additional_idx < len(s):
                    ans += s[j] + s[additional_idx]
                else:
                    ans += s[j]

        for i in range(numRows - 1, len(s), (numRows - 1) * 2):
            ans += s[i]

        return ans
