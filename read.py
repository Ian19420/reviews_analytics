data = []
count = 0
with open('reviews.txt') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(f'檔案讀取完了，總共有{len(data)}筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print(f'留言平均長度為:{sum_len/len(data)}')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(f'一共有{len(new)}筆資料長度小於100')


good = []
for d in data:
	if "good" in d:
		good.append(d)
print(f'一共有{len(good)}筆資料提到good')
#good = [d in d in data if "good" in d] 進階寫法

bad = []
for d in data:
	if "bad" in d:
		bad.append("bad" in d)
print(f'一共有{len(bad)}筆資料提到bad')
#bad = ["bad" in d for d in data] bad是否在data裡

