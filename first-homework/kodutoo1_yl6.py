from itertools import groupby

S = input()
groups = []
# grupeerin jarjest minevad samad numbrid uhte listi
for number, group in groupby(S):
    groups.append(list(group))

# kain listis olevad samaliikmelised listid labi ning votan uhe elemendi ja listi pikkuse
for group in groups:
    group_element = group[0]
    group_length = len(group)
    print(f"({group_length}, {group_element})", end=' ')

