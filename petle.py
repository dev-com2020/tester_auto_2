jezyki = ["C", "Python", 'Java']
cyfry = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# print("Języki programowania:")
# for x in range(len(jezyki)):
#     # print(jezyki[x])
#     print(f'Języki: {jezyki[x]}')
#
# for x in range(1,len(cyfry),2):
#     # print(f'Cyfry: {cyfry[x]}')
#     print(cyfry[x])
#
# print(*cyfry, sep='-')
# print(cyfry)


# for p in range(3):
#     for q in range(4):
#         if q == 2:
#             print(f'Pomijam q={q}')
#             continue
#     print(f'(p={p}, q={q})')
#
# for p in range(len(jezyki)):
#     for q in range(len(cyfry)):
#         if q == 2:
#             print(f'Pomijam q={cyfry[q]}')
#             break
#     print(f'(p={jezyki[p]}, q={cyfry[q]})')

# i = 1
# tmp = 0
# while i <= 100:
#     tmp = tmp + i
#     i = i + i
# print("Suma liczb od 1 do 99", tmp)

while True:
    print("Menu:")
    print("1. policz")
    print("2. wyjdź")
    print("------")
    wybor = input("Wybierz opcje:")
    if wybor == "1":
        print("Suma:", 50 + 55)
    elif wybor == "2":
        break
    else:
        print("Nieznana opcja!")


