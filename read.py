data = []
count = 0
with open('reviews.txt') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(f'檔案讀取完了，總共有{len(data)}筆資料')

