# 检查常用Python库版本号

import scipy # 导入 SciPy 库。
#SciPy 是一个用于科学计算和数据分析的开源 Python 库，它包含了许多用于数学、科学和工程计算的功能和工具。
#'scipy: %s' 是一个包含占位符的字符串，其中%s 是一个占位符，表示后面将被替换成一个字符串的值。
#scipy.__version__是 SciPy 库的一个属性，它包含了当前导入的 SciPy 版本的字符串。通过scipy.__version__，我们可以获取计算机中当前 SciPy 库的版本信息。
print('scipy: %s' % scipy.__version__)


import numpy
#在 Python 中用于导入 NumPy 库的语句。NumPy 是 Python 中用于科学计算和数值操作的一个强大的开源库。它提供了多维数组 (NumPy array) 和一系列用于操作这些数组的函数。
#NumPy 广泛用于数据分析、科学计算、机器学习等领域。
print('numpy: %s' % numpy.__version__)


import matplotlib
#导入 Matplotlib 库的语句。Matplotlib 是一个用于创建各种类型的图形和可视化的Python 库。

print('matplotlib: %s' % matplotlib.__version__)


import pandas
#导入 Pandas 库。Pandas 是 Python 中用于数据分析和数据操作的高性能库。
#Pandas 提供了两种主要数据结构：Series 和 DataFrame，用于处理和操作各种类型的数据，包括表格数据、时间序列数据等等。


print('pandas: %s' % pandas.__version__)


import statsmodels
#导入 Statsmodels 库。
#Statsmodels 是一个 Python 库，用于执行统计分析和建立统计模型，包括线性回归、时间序列分析、假设检验和许多其他统计方法。
print('statsmodels: %s' % statsmodels.__version__)


import sklearn
#导入 Scikit-Learn 库。Scikit-Learn，也称 sklearn，是一个强大的开源机器学习库
#提供了用于各种机器学习任务的工具和算法。它包括分类、回归、聚类、降维、模型选择、模型评估等各种机器学习任务的实现。Scikit-Learn 还包括用于数据预处理和特征工程的功能。
print('sklearn: %s' % sklearn.__version__)

