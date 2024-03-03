# 统计学python课

## 3月3日答疑

Q1: 这门课希望学生对python掌握哪些能力？

### 数据处理
统计学方法理论(课件、样例代码)
package工具：pandas(表格), numpy(矩阵运算)，statmodel(统计学模型)
达到的能力：excel来求解和、差、多列的运算得到新的数据列，标准化、缺失值处理、stata、SASS

### 数据分析

1.简单分析：用describe函数去查看EDA统计信息，离散值的频数
2.指标：特征重要性(sklearn)去筛选建模的变量(线性回归)
3.建模后解释结果...(非常多的工具包)

### 数据可视化

1.基于matplotlib的作图指令（饼图、直方图、散点图）
2.追求一些复杂的可视化
- 地图可视化echarts的python化, geopandas
- 知识图谱neo4j --> 节点(点)+关系(线) 在一个平面上可视化
3.咨询（非常diy，等于代码指令，论文的流程图）：swot、横轴坐标上面加一些文字、瀑布图

Q2: 在终端运行python代码，发现No such file的报错，无法加载数据

解法1：将代码文件里的../../data/msleep.csv 改成data/msleep.csv
解法2: 在你用命令行执行python进入ide界面前，先通过cd src/example的指令进入到和代码相同的文件夹下,再用python指令进入ide界面