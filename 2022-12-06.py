with open('input_artifacts/2022-12-06-A-input.txt','r') as c:
    data = c.read()
dd = list(data)

def find_marker(dd, length=4):
    for n,i in enumerate(dd):
        if n < length:
            continue
        if len(set(dd[n-length:n])) == length:
            return n
    raise RuntimeError('No message found.')
    
print('part 1: ', find_marker(dd, 4))
print('part 2: ', find_marker(dd, 14))
