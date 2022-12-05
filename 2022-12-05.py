from textwrap import wrap

def clean_construct(object):
    obj = [list(filter(lambda n: n != '    ', x[::-1])) for x in list(zip(*object))]
    return obj

def construct_last(construct):
    outstring = ''
    for x in construct:
        outstring += x[-1].replace('[','').replace(']','').strip()
    return outstring
    

def parse_input(data):
    moves = []
    construct = []
    for line in data:
        if '[' in line and ']' in line:
            
            construct.append(wrap(line,4, replace_whitespace=False, drop_whitespace=False))
        elif 'move' in line:
            moves.append([int(x) for x in line.split(' ')[1::2]])
        elif '1   2   3' in line: numbins = max([int(x) for x in line.split()])
    return moves, clean_construct(construct), numbins
    
def move_items(source, target, amount: int, crane_type:int):
    s = source[:]
    t = target[:]
    if amount > len(s):
        raise ValueError('Cannot move more than source has available')
    if crane_type == 9000:
        t += s[-amount:][::-1]
    elif crane_type == 9001:
        t += s[-amount:]
    else:
        raise ValueError('Crane Type unrecognized')
    s = s[:-amount]
    return s, t

def construct_update(move, obj, crane_type:int = 9000):
    source = obj[move[1]-1]
    target = obj[move[2]-1]
    amount = move[0]
    s, t = move_items(source, target, amount, crane_type)
    obj[move[1]-1] = s
    obj[move[2]-1] = t
    return obj

def part(crane_type):
    with open('input_artifacts/2022-12-05-A-input.txt','r') as c:
        data = c.read().split('\n')

    moves, construct, numbins = parse_input(data)
    construct_operation = construct[:]

    for m in moves:
        construct_operation = construct_update(m, construct_operation[:], crane_type)
    return construct_last(construct_operation)

print('part1: ', construct_last(part(9000)))
print('part2: ', construct_last(part(9001)))
    