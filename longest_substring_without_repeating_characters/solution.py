class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_start_idx = 0
        substring_end_idx = 0


        max_substring_length = 0
        letters = {}

        for i in range(len(s)):
            if letters.get(s[i]) is None:
                letters[s[i]] = i
            elif letters[s[i]] >= substring_start_idx and letters[s[i]] < substring_end_idx:
                substring_start_idx = 1 + letters[s[i]] 

            letters[s[i]] = i
            substring_end_idx = i + 1

            for i in range(len(s)):
                if substring_start_idx == i:
                    print("|", end="")
                elif substring_end_idx == i:
                    print("|", end="")
                else:
                    print("", end=" ")   
                print(s[i], end="")
            print("")
            max_substring_length = max(max_substring_length, substring_end_idx - substring_start_idx)

        return max_substring_length 
            

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("bbbbb"))

# "abcaabcbb"