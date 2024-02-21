import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# 按照Category列的值分组，并计算每个分组的总和
grouped = df.groupby('Category').sum()

print(grouped)
