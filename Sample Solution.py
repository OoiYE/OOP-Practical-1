f = open('A1_input.txt', 'r')
lines = f.readlines()
f.close()

result = []

for line in lines:
    items = line.split('[')
    for item in items[1:]:
        data = item.split(']')[0].replace("'", "").replace(' ', '').replace(
            '1', 'One').replace('2', 'Two').replace('3', 'Three')
        result = result + [data]
    print(data)
