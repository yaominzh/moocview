[toc]
# chap01
## 08 aggregate
常见步骤

| 步骤 | 作用 | SQL等价运算符
| --- | --- | ---
| $match | 过滤 | WHERE
| $project | 投影 | AS
| $sort | 排序 | order by
| $group | 分组 | group by
| $skip/$limit | 结果限制 | SKIP/LIMIT
| $lookup | 左外连接 | Left out join
| --- | --- | ---
| $unwind | 展开数组 | n/a
| $graphLookup| 图搜索 | n/a
| $facet/$bucket | 分面搜索 | n/a


聚合查询可以用于OLAP和OLTP的场景

| OLTP | OLAP
| --- | ---
| 计算  | - 分析一段时间内的销售总额、均值
|   | - 分析一段时间内的销售总额、均值
|   | - 计算一段时间内的净利润
|   | - 分析购买人的年龄分布
|   | - 分析学生成绩分布
|   | - 统计员工绩效