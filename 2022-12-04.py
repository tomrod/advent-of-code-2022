def covered(x0, x1):
    return x0[0] <= x1[0] and x0[1] >= x1[1]    

def overlap(x0, x1):
    return x0[0] <= x1[0] <= x0[1] <= x1[1]

def pair_assignment(data_input):
    assignments = [[int(z) for z in y.split('-')] for y in data_input.split(',')]  
    elf0 = sorted(assignments[0])
    elf1 = sorted(assignments[1])
    return elf0, elf1

def coverage_check(data_input):
    elf0, elf1   = pair_assignment(data_input)
    return covered(elf0, elf1) or covered(elf1, elf0)

def overlap_check (data_input):
    elf0, elf1 = pair_assignment(data_input)
    cover = coverage_check(data_input)
    overlaps = overlap(elf0,elf1) or overlap(elf1, elf0)
    return cover or overlaps
    
# Run process

with open('input_artifacts/2022-12-04-A-input.txt','r') as c:
    data = c.read().split('\n')
    
cover_cnt = 0
overlap_cnt = 0
for d in data:
    cover_cnt += coverage_check(d)
    overlap_cnt += overlap_check(d)
    
print('part1: ', cover_cnt)
print('part2: ', overlap_cnt)