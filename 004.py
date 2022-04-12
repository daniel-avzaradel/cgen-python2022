## 12/04/2022 - 4th meeting

# zip function

ids = [12, 23, 34, 14, 16]
names = ['moshe', 'daniel', 'laura', 'paola']
data = zip(ids, names)

print(type(data))

for item in data:
    print(item)