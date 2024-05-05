class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        left_idx = 0
        right_idx = 0
        for i in range(len(height)):
            if height[i] == 0:
                continue

            skip_ahead = ans // height[i]
            skip_ahead = skip_ahead if skip_ahead < len(height) else len(height)
            for j in range(i + skip_ahead, len(height)):
                ans = max(ans, (j - i) * min(height[i], height[j]))

        return ans


if __name__ == "__main__":
    test = [1,8,6,2,5,4,8,3,7]

    print(Solution().maxArea(test))
