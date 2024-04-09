# def print_rangoli(size):
#     alifbo = 'abcdefghijklmnopqrstuvwxyz'
#
#     for i in range(size - 1, 0, -1):
#         row = ['-'] * (2 * size - 1)
#         for j in range(size - i):
#             row[size - 1 - j] = alifbo[j + i]
#             row[size - 1 + j] = alifbo[j + i]
#         print('-'.join(row))
#     for i in range(0, size):
#         row = ['-'] * (2 * size - 1)
#         for j in range(0, size - i):
#             row[size - 1 - j] = alifbo[j + i]
#             row[size - 1 + j] = alifbo[j + i]
#         print('-'.join(row))
#
#
# n = int(input().strip())
# print_rangoli(n)






