# 1. numpy库
import numpy as np
a = [1, 2, 3]  # 创建数组
b = np.array(a) # 将a转为array格式
c = np.ones([3,5],dtype=np.int)  # 创建数值为1的，维度为3×5的整形数组
d = np.zeros([3,5],dtype=np.int)  # 创建数值为0的，维度为3×5的整形数
e = np.full([3,5],5,dtype=np.int)  # 创建数值为5（该数值为人工指定）的，维度为3×5的整形
f = np.eye(5)    # 创建维度为5的方阵
g = np.random.rand(5,6,7)  # 创建shape为（5,6,7）的数组，数值范围在0-1之间的随机数
h = np.random.uniform(0, 100, size=(5,6))  # 创建shape为（5,6）的数组，数值范围在0-100之间的随机数
i = np.random.randint(0, 100, size=(5,6))  # 创建shape为（5,6）的整形数组，数值范围在0-100之间的随机整数
j = np.arange(5,100,10)  # 创建一个从5开始，间隔为10，结束于小于100的等差数列
k = np.linspace(5,100,50) # 创建50个在闭区间[5,100]内均匀分布的值
k2 = np.expand_dims(c,axis=0) # 在数组k的最左侧增加一个维度
k3 = np.expand_dims(c,axis=-1) # 在数组k的最右侧增加一个维度
k4 = np.expand_dims(c,axis=2) # 在数组k的index=2处增加一个维度
k5 = k % 3  # 求除以3的余数
np.sort(array_name)   # 数组整体排序
np.sort(array_name,axis=0)  # 数组仅对行排序
np.sort(array_name,axis=1)  # 数组仅对列排序
l = c[:2,2:4].copy()    # 数组索引后复制。也可写作np.copy()
np.unique(array_name)   # 提取唯一元素
array_name.T      # 数组转置
array_name.reshape(3,2,2) # 改变数组形状，新shape的各维度相乘应与旧的相等，不想算的可以用-1表示
array_name.resize(3,2,2) # 改变数组形状，新shape的各维度相乘可以不与旧的相等，不足的补0
np.where(condition,x,y)  # 条件运算，数组中符合条件condition的更改为数值x，不符合的改为y
result = np.amax(array_name,axis=0)  # 求矩阵中每一列的最大值。axis=1表示按照行来求。整个矩阵求最大值的话，不用谢axis参数
np.amin(array_name)  # 求矩阵最小值。参数含义同np.amax
np.mean(array_name,dtype=np.int)  # 求矩阵平均值。参数含义同np.amax
np.std(array_name)  # 求矩阵方差。参数含义同np.amax
result = np.vstack(v1,v2) # 两个列数相同的矩阵v1和v2的拼接
result = np.hstack(v1,v2) # 两个行数相同的矩阵v1和v2的拼接
result = np.append(array_name, [0, 2])   # 末尾添加元素
result = np.append(array_name, [[0, 2, 11]], axis=0)  # 最后一行添加一行
result = np.append(array_name,[[0], [2], [11]], axis=1) # 最后一列添加一列（注意添加元素格式）
result = np.insert(array_name, 1, [[11, 12, 10]], axis=0) # 在索引位置为1的位置插入一行
result = np.insert(array_name, 1, [[11, 12, 10]], axis=1)  # # 在索引位置为1的位置插入一列
np.load(fname,dtype,comments='#',delimiter=None,skiprows=0,usecols=None)
# 其中，fname:读取的文件、文件名；dtype：数据类型；comments：注释；delimiter：分隔符，默认是空格
# skiprows：跳过前几行读取，默认是0；usecols：读取哪些列，usecols=（1， 2， 5）读取第1,2,5列

# 2. xarray库
import xarray as xr
data = xr.open_dataset(file_name) # 读取nc文件
t2m  = data['t2m']     # 从data中提取所需变量
xr.concat([data2018, data2019], dim='time') # 维度拼接
xr.merge([data2018.u10, data2019.t2m])  # 变量合并
data.mean(dim=['latitude', 'longitude']) # 对经纬度进行平均
data.std(dim='time')  # 对时间维度求方差
data.groupby('time.season').min(dim='time')  # 月平均转季节数据
data.groupby('time.year').min(dim='time')  # 月平均转年数据

# 3. pandas库
import pandas as pd
data = pd.DataFrame()  # 定义一个空的DataFrame格式数据
data['增加的维度'] = np.array格式的数据  # 向data中添加数据。也可以直接定义好，如下：
data = pd.DataFrame({"实况降水":np.array(pre_obs),
                     "IR39":np.array(b07),
                     "IR62":np.array(b08),
                     "IR70":np.array(b09),
                     "IR73":np.array(b10)})

# 4. 列表
import numpy as np
a_list = []  # 定义一个空列表
a_list.append() # 在列表最后添加元素
a_list = [str(i)+'元素' for i in range(10)] # 用循环的形式为列表赋值
list1+list2  # 列表合并，等价于list1.extend(list2)
a_array = np.array(a_list) # 将列表转为array格式
