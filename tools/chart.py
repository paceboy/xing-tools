
"""
    通过表格数据生成曲线图
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rcParams

def draw_chart():
    font_path = "/System/Library/Fonts/Supplemental/Songti.ttc"  # MAC系统下的黑体路径
    rcParams['font.sans-serif'] = font_manager.FontProperties(fname=font_path).get_name()

    # 数据
    concurrency = ["2", "4", "6", "8"]
    peak_2024 = [61.8, 73.1, 76.1, 82.6]
    avg_2024 = [46.7, 49.5, 51.3, 54.1]
    peak_2023 = [57.1, 64.3, 81, None]  # 8万无数据，用 None 表示
    avg_2023 = [47.5, 58.7, 50, None]  # 8万无数据，用 None 表示

    # 绘制折线图
    plt.figure(figsize=(10, 6))

    # 2024 年
    plt.plot(concurrency, peak_2024, label="2024年峰值", marker="o")
    plt.plot(concurrency, avg_2024, label="2024年平均值", marker="o")

    # 2023 年
    plt.plot(concurrency, peak_2023, label="2023年峰值", marker="o", linestyle="--")
    plt.plot(concurrency, avg_2023, label="2023年平均值", marker="o", linestyle="--")

    # 在曲线末尾添加文字说明
    plt.text(len(concurrency) - 1 + 0.03, peak_2024[-1], '2024年峰值', fontsize=12, color='blue', va='center', ha='left')
    plt.text(len(concurrency) - 1 + 0.03, avg_2024[-1], '2024年平均值', fontsize=12, color='green', va='center', ha='left')
    plt.text(len(concurrency) - 2 + 0.03, peak_2023[-2], '2023年峰值', fontsize=12, color='orange', va='center', ha='left')  # 使用倒数第二个点
    plt.text(len(concurrency) - 2 + 0.03, avg_2023[-2], '2023年平均值', fontsize=12, color='red', va='center', ha='left')    # 使用倒数第二个点


    # 图表标题和标签
    plt.title("2023年与2024年入口总请求量对比", fontsize=16)
    plt.xlabel("并发（万）", fontsize=16)
    plt.ylabel("总请求量 (万)", fontsize=16)
    plt.legend()
    plt.grid(alpha=0.5)

    # 显示图表
    plt.show()