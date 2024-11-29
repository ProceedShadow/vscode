# 案例：找到和大于等于 target 的最小子数组长度

# 问题描述
# 给定一个正整数数组 nums 和一个目标值 target，找到一个最小长度的连续子数组，使得这些子数组的和大于等于 target。如果不存在这样的子数组，返回 0。

# 输入
# nums = [2, 3, 1, 2, 4, 3]
# target = 7

# 输出
# 2

# 解释
# 因为最小长度的子数组是 [4, 3]，其和为 7。

# ------------------------------------------------------------------------------------------------------------------------------------------------ #

# 代码实现
def min_array_length(nums: list, target: int) -> int:
    """
    获取最短连续子数组，使其所有元素和大于或等于target。
    :param nums: 正整数数组
    :param target: 目标值
    :return 最短子数组长度
    """
    slow = 0
    cur_sum = 0
    min_len = len(nums)
    for fast, num in enumerate(nums):
        # 每次加和窗口中的元素
        cur_sum += num
        # 判断当前窗口中元素是否达到目标值
        while cur_sum >= target:
            # 更新窗口长度
             min_len = min(min_len, fast - slow + 1)
             cur_sum -= nums[slow]
             slow += 1
    # 超过数组大小返回0
    return min_len if min_len <= len(nums) else 0