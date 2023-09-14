class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matching_strings = []
        for regular_expression_idx in range(len(p)):
            previous_step = matching_strings
            matching_strings = []
            current_regex_char = p[regular_expression_idx]
            if len(previous_step) == 0:
                if regular_expression_idx != 0:
                    return False

                if current_regex_char.isalpha():
                    if current_regex_char == p[0]:
                        matching_strings.append(p[0])
                
                elif current_regex_char == '.' and len(s) != 0:
                    matching_strings.append(s[0])

                elif current_regex_char == '*':
                    for idx in range(1, len(s)):
                        matching_strings.append(s[:idx])


            elif current_regex_char.isalpha():
                for string in previous_step:
                    if len(string) < len(s) and s[len(string)] == current_regex_char:
                        matching_strings.append(string + s[len(string)])

            elif current_regex_char == ".":
                for string in previous_step:
                    if len(string) < len(s):
                        matching_strings.append(string + s[len(string)])
                        
            elif current_regex_char == '*':
                for idx in range(len(previous_step[0]), len(s) + 1):
                    matching_strings.append(s[:idx])

            # print(f"Iteration {regular_expression_idx}: {matching_strings}")

        for string in matching_strings:
            if string == s:
                return True
        
        return False
        

if __name__ == "__main__":
    print(Solution().isMatch("ab", ".*"))
