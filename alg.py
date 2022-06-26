pages=int(input("Number of pages: "))
rawInput=list(range(1,pages+1))
output = list()
lastI = 0
offset = [4, -5, 2, -3,]
polowa = int(round(len(rawInput)/2,1))

print(rawInput)

for raw in rawInput:
    output.append(raw + offset[lastI])
    if lastI<len(rawInput):
        lastI = lastI + 1

print(output)

#  1,  2,  3,  4,  5,  6,  7,  8, |  9,  10,  11,  12,  13,  14,  15,  16     wejscie
#  1,  3,  5,  7,  4,  2,  8,  6, |  9,  11,  13,  15,  12,  10,  16,  14     wyjscie
#                                 | 
#  0,  4, -1,  1, -2,  2, -3, -1, |  0,   4,  -1,   1,  -2,   2,  -3,  -1     przesuniecia
#     +4, -5, +2, -3, +4, -5, +2         +4,  -5,  +2,  -3,  +4,  -5,  +2     dodania, odjecia