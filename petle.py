jezyki = ["C", "Python", 'Java']
cyfry = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Języki programowania:")
for x in range(len(jezyki)):
    # print(jezyki[x])
    print(f'Języki: {jezyki[x]}')

for x in range(1,len(cyfry),2):
    # print(f'Cyfry: {cyfry[x]}')
    print(cyfry[x])

print(*cyfry, sep='-')
print(cyfry)