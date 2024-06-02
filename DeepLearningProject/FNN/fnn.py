import numpy as np

np.random.seed(42)

# 输入层 -> 隐藏层
input_size = 3  # 输入维度
hidden_size = 4  # 隐藏层神经元数
output_size = 1  # 输出维度

# 初始化权重和偏置
W1 = np.random.rand(input_size, hidden_size)
b1 = np.random.rand(1, hidden_size)
W2 = np.random.rand(hidden_size, output_size)
b2 = np.random.rand(1, output_size)

def predict(x):
    return x