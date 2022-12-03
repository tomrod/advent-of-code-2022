def score1(info : list):
    match = ''.join(info)
    your_play = info[1]
    their_play = info[0]
    score_player = {'X':1, 'Y':2, 'Z':3}[your_play]
    win = ['AY','BZ','CX']
    draw = ['BY','CZ','AX']
    lose = ['CY','AZ','BX']
    if match in win:
        score_match = 6
    elif match in draw:
        score_match = 3
    elif match in lose:
        score_match = 0
    return score_match + score_player

def score2(info : list):
    match_scores = [0,3,6]
    outcome_index = 'XYZ'.index(info[1])
    outcome_score = match_scores[outcome_index]
    play_strats = {'A':'CAB','B':'ABC', 'C':'BCA'}[info[0]][outcome_index]
    play_score = {'A':1,'B':2,'C':3}[play_strats]
    return outcome_score + play_score
    

with open('input_artifacts/2022-12-02-A-input.txt','r') as cc:
    data = [x.strip().split(' ') for x in cc.readlines()]
    scores1 = [score1(y) for y in data]
    scores2 = [score2(y) for y in data]
    
print('part1: ', sum(scores1))    
print('part2: ', sum(scores2))

for a in 'ABC' :
    for x in 'XYZ':
        print(a,x,score2([a,x]))