import pandas as pd
import numpy as np
from pymongo import MongoClient

# 属性
# df.shape
# df.dtypes
# df.ndim  数据维度
# df.index
# df.columns
# df.index
# df.values 对象值
# 查询
# df.head()
# df.tail()
# df.info()
# df.describe()


# client = MongoClient()
# collection = client["douban"]["tv1"]
# data = list(collection.find())
# t1 = data[0]
# data = pd.Series(t1)

# DataFrame 二维，series容器
# x = pd.DataFrame(np.arange(12).reshape(3,4), index=list("abc"),columns=list("xczy"))
# print(pd.DataFrame(data))

# series
# t = pd.Series(np.arange(10),index=list("abcdefghij"))

# pandas.read_csv()读取csv文件
data = pd.read_csv("./job_report.csv")
df = pd.DataFrame(data)
# data = pd.read_clipboard()

# pandas.DataFrame.info()
data = df.info()
print(df.dtypes)
