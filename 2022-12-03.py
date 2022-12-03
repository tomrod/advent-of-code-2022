import string

letters = {x:y for x, y in zip(string.ascii_letters, range(1,len(string.ascii_letters)+1))}

def scoring1(line):
    ll = int(len(line)/2.)
    line1 = line[:ll]
    line2 = line[ll:]
    shared1 = [x for x in line1 if x in line2]
    type_sum = sum([letters[z] for z in set(shared1)])
    return type_sum

def scoring2(lines):
    shared = set(lines[0]).intersection(set(lines[1])).intersection(set(lines[2]))
    if len(shared)==0:
        raise ValueError('No shared letters')
    return sum([letters[z] for z in set(shared)])
    
with open('input_artifacts/2022-12-03-A-input.txt','r') as cc:
    c =  [x.strip() for x in cc.readlines()]
    
score2 = 0
for n in range(0,len(c),3):
    lines = c[n:n+3]
    score2 += scoring2(lines)    
    
print('part1: ', sum([scoring1(line) for line in c]))
print('part2: ', score2)