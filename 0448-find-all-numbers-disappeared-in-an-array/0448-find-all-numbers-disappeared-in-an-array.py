class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        # Mark visited numbers
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Numbers that remain positive are missing
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result