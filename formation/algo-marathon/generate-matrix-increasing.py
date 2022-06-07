

def generateSequence(target):
    if target == 0:
        return []

    count = 0 # 1
    arr = []
    mx = []

    while len(arr) < target:
        if arr == []:
            arr.append(target-1)
        else:
            arr.append(target)
        count =+ 1
        mx.append(arr)
    print("mx: ", mx)
    print("count: ", count)
    print("target: ", target)
    # print("arr length: ", len(arr))

target2 = 2
target3 = 3
target4 = 4
print(generateSequence(target2))
# print(generateSequence(target3)) # [ [1], [1, 2], [1, 2, 3]]
# print(generateSequence(target4)) # [ [1], [1, 2], [1, 2, 3], [1, 2, 3, 4] ]

# [
#   [1],
#   [1, 2]
# ]
#    given target = 2, create array spanning 1..target
