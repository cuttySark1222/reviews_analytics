data = [] # 创建空 list 来储存每一笔留言
review_len = 0 # 声明变量，用来计算留言的总长度

with open('reviews.txt', 'r') as f: # 打开留言文件
	for line in f: # 把每一笔留言分开存储到预设好的 list 里面
		data.append(line)

for i in data: # 计算留言总长度
	review_len += len(i)

avg_review_len = review_len / len(data) # 计算留言平均长度

data_less_100 = [d for d in data if len(d) < 100] # 用 List Comprehension 写法
# for d in data:
# 	if len(d) < 100:
# 		data_less_100.append(d)


print(f'文档中总共有{len(data)}笔留言。')
print(f'平均留言长度为：{avg_review_len}')
print(f'总共有{len(data_less_100)}笔留言长度小于100')