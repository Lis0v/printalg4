pages=int(input("Number of pages: "))
pages_list=list(range(1,pages+1))

i = 0



# 1,  2,  3,  4,  5,  6,  7,  8, | 9,  10,  11,  12,  13,  14,  15,  16     wejscie
# 1,  3,  5,  7,  4,  2,  8,  6, | 9,  11,  13,  15,  12,  10,  16,  14     wyjscie
#                                |
# 0,  4, -1,  1, -2,  2, -3, -1, | 0,   4,  -1,   1,  -2,   2,  -3,  -1     przesuniecia
#     4, -5,  2, -3,  4, -5,  2         4,  -5,   2,  -3,   4,  -5,   2     dodania, odjecia