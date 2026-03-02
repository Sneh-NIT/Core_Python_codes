import random
p1_score = 0
p2_score = 0
sb = [0, 6, 2, 1, 3, 'out', 4]
i = 0
ball_result = 0
while i < 6:
    ball_result = random.choice(sb)
    if ball_result != 'out':
        p1_score = p1_score + ball_result
    else:
        break
    i += 1
i = 0
while i < 6:
    ball_result = random.choice(sb)
    if ball_result != 'out':
        p2_score = p2_score + ball_result
    else:
        break
    i += 1
print(f"Player 1 score: {p1_score}")
print(f"Player 2 score: {p2_score}")
if p1_score < p2_score:
    print("Player 2 wins")
elif p1_score > p2_score:
    print("Player 1 wins")
else:
    print("Match is drawn")