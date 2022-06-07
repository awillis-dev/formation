def canMatchFellows(input):
    skillSet = set()

    for skillLevel in input:
        skill = input[skillLevel]
        if skill in skillSet:
            skillSet.remove(skill)
        else:
            skillSet.add(skill)


    return len(skillSet) == 0

map1 = {}
map2 = {"oliver": 1}
map3 = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
map4 = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}

print(canMatchFellows(map1))
print(canMatchFellows(map2))
print(canMatchFellows(map3))
print(canMatchFellows(map4))
