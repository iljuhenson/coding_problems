class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid_subseq_len: list[int] = []

        for c in s:
            if c == "(":
                valid_subseq_len.append(0)
            elif c == ")":
                if len(valid_subseq_len) > 0 and valid_subseq_len[-1] == 0:
                    valid_subseq_len.pop(-1)
                    valid_subseq_len.append(2)

                elif len(valid_subseq_len) > 1 and valid_subseq_len[-2] == 0:
                    tmp: int = valid_subseq_len.pop(-1)
                    valid_subseq_len.pop(-1)
                    valid_subseq_len.append(tmp + 2)

                else:
                    valid_subseq_len.append(-1)
                    continue

                if len(valid_subseq_len) > 1 and valid_subseq_len[-2] != 0 and valid_subseq_len[-2] != -1:
                    tmp1: int = valid_subseq_len.pop(-1)
                    tmp2: int = valid_subseq_len.pop(-1)

                    valid_subseq_len.append(tmp1 + tmp2)

        if len(valid_subseq_len) != 0:
            return max(max(valid_subseq_len), 0)
        else:
            return 0
        

if __name__ == "__main__":
    s = ")"

    print(Solution().longestValidParentheses(s))