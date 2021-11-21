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