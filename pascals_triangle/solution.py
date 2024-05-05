from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_list = [[1]]
        for i in range(1, numRows):
            line_list = [1,]

            for j in range(1, i):
                line_list.append(pascal_list[i - 1][j] + pascal_list[i - 1][j - 1] )

            line_list.append(1)
            pascal_list.append(line_list)

        return pascal_list

if __name__ == "__main__":
    print(Solution().generate(2))
