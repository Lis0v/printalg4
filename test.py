rawInput = [0,0,0,0,0,0,0]
offsets = [1, 1, 1, -1, 0, 1]
output = list()
lastI = 0

for raw in rawInput:
    output.append(raw + offsets[lastI])
    if lastI<len(rawInput):
        lastI = lastI + 1

print(output)