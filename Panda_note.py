import pandas as pd
import numpy as np
from pymongo import MongoClient

# 属性
# 查询
# client = MongoClient()
# DataFrame 二维，series容器
# pandas.read_csv()读取csv文件
# pandas.DataFrame.info()
# dataframe中排序的方法 df.sort_values


#    属性
# df.shape
# df.dtypes
# df.ndim  数据维度
# df.index
# df.columns
# df.index
# df.values 对象值
#    查询
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
# data = pd.read_csv("./job_report.csv")
# df = pd.DataFrame(data)
# data = pd.read_clipboard()

# pandas.DataFrame.info()
# data = df.info()

# dataframe中排序的方法 df.sort_values
# data = df.sort_values(by="All",ascending=False)

###  pandas 取行或者列 df.loc通过标签索引 df.iloc通过位置索引
# data = {"a":[1,2,4,7],"b":[3,6,7,9],"c":[3,4,6,8]}
# df = pd.DataFrame(data)
# # df[:10]
# # # df["Staff Role"]
# print(df)
# x = df.loc[:,["a","b"]]
# print(x)

### 使用次数超过3次
# data = pd.read_csv("./job_report.csv")
# df = pd.DataFrame(data)
# print(df)
# count = df[df["Questionnaire/DG"]>2] # Questionnnaire/DG里数值大于2的行
# print(count)
# print(df[(50>df["All"])&(df["All"]>2)])  # Questionnnaire/DG里数值在【2，50】间的行

### 缺失数据的处理 pd.isnull(df)判断NaN的数据 pd.notnull(df)
#   处理方式1：删除所在行 dropna(axis=0,how='any',inplace=False)
#   处理方式2：填充数据 t.fillna(t.mean()),t.fiallna(t.median()),t.fillna(0)
# data = pd.read_csv("./job_report.csv")
# df = pd.DataFrame(data)
# print(pd.isnull(df))  # 判断NaN的数据 是NaN --> True
# print(df.fillna(df.mean()))
# df["Questionnaire/DG"] = df["Questionnaire/DG"].fillna(df["Questionnaire/DG"].mean())
# print(df)

### 构建全是0的数组
data = pd.read_csv("./job_report.csv")
df = pd.DataFrame(data)
zeros_df = pd.DataFrame(np.zeros((df.shape[0], 1000)))
print(zeros_df)
print(df.shape[0])
