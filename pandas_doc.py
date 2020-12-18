import pandas as pd
import numpy as np

data = pd.read_csv("job_report.csv", skiprows=[1])  # skiprows : will skip row 1
statistic = data.describe()  # 计算基本的统计数据
head = data.head(3)  # 查看前3行的数据
loc = data.loc[2]  # 打印出第2行
data["Fieldwork"].value_counts()  # 统计出现的次数

# 绘图
# data["Fieldwork"].plot()

s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20201218', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20201225'),
    'C': np.array([3]*4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})

print(df2)