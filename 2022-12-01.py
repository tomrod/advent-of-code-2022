from collections import Counter

# copied user-specific input to input_artifacts/2022-12-01-A-input.txt
with open('input_artifacts/2022-12-01-A-input.txt','r') as cc:
    data = [int(x.strip()) if x != '\n' else '' for x in cc.readlines()]

elf_id = 0
elves_calories = {}
for line in data:
    if line == '':
        elf_id += 1
    elif isinstance(line, int):
        elves_calories[elf_id] = elves_calories.get(elf_id, 0) + line

max_ = max(elves_calories.values())
        
print('part1:', max_)

c = sum([x[1] for x in Counter(elves_calories).most_common(3)])

print('part2:', c)