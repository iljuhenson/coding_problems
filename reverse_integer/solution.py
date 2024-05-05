class Solution:
    def reverse(self, x: int) -> int:
        number_as_string = str(x)
        max_number_as_string = "2147483647"
        #                      -2147483412
        if(x < 0):
            number_as_string = number_as_string[1:]

        if len(number_as_string) > 10:
            return 0
        elif len(number_as_string) == 10:
            for i in range(9, -1, -1):
                if int(number_as_string[i]) > int(max_number_as_string[9 - i]):
                    return 0
                elif int(number_as_string[i]) == int(max_number_as_string[9 - i]):
                    continue
                else:
                    break
        
        reversed_number_as_string = ''
        for i in range(len(number_as_string) - 1, -1, -1):
            # print(i)
            reversed_number_as_string += number_as_string[i]

        return int(reversed_number_as_string if x >= 0 else f"-{reversed_number_as_string}")


if __name__ == "__main__":
    print(Solution().reverse(-2147483412))
